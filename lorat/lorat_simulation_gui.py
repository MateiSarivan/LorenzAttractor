import os
import tkinter
import timeit
import csv
import json
import fractions
import uuid
import numpy as np

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

from lorat.lorenz import euler
from lorat.plotting import graph
from lorat.pdf_gen import generate_pdf
from lorat.pdf_merge import merge_pdfs

class LoratGUI:
    def __init__(self):
        
        self.file_address = None
        self.experiment_data = {}
        dir_path = os.path.dirname(os.path.realpath(__file__))
        json_file = open(os.path.join(dir_path, 'json', 'configuration.json'))
        data = json.load(json_file)
        self.range_N = np.linspace(start = data['configuration']['N']['min'], stop = data['configuration']['N']['max'], num = 100, dtype = int)
        self.range_dt = np.linspace(start = data['configuration']['dt']['max'], stop = data['configuration']['dt']['min'], num = 100)
        self.range_initial_x = np.linspace(start = data['configuration']['x']['min'], stop = data['configuration']['x']['max'], num = 100)
        self.range_initial_y = np.linspace(start = data['configuration']['y']['min'], stop = data['configuration']['y']['max'], num = 100)
        self.range_initial_z = np.linspace(start = data['configuration']['z']['min'], stop = data['configuration']['z']['max'], num = 100)
        self.list_sigma = np.float_(data['configuration']['sigma'])
        self.list_beta = [float(fractions.Fraction(x)) for x in data['configuration']['beta']] #transform beta to float
        self.list_rho = np.float_(data['configuration']['rho'])
        self.list_beta_string = data['configuration']['beta']
        json_file.close()


        self.root = tkinter.Tk()
        self.root.geometry("1366x768")
        self.root.wm_title("Embedding in Tk")

        fig = Figure(figsize=(10, 5), dpi=100)
        self.subplots = []
        self.subplots.append(fig.add_subplot(2, 3, 1, projection = '3d'))
        self.subplots.append(fig.add_subplot(2, 3, 2, projection = '3d'))
        self.subplots.append(fig.add_subplot(2, 3, 3, projection = '3d'))
        self.subplots.append(fig.add_subplot(2, 3, 4, projection = '3d'))
        self.subplots.append(fig.add_subplot(2, 3, 5, projection = '3d'))

        for (subplot, sigma, beta, rho) in zip(self.subplots, self.list_sigma, self.list_beta_string, self.list_rho):
            subplot.set_xlabel('x')
            subplot.set_ylabel('y')
            subplot.set_zlabel('z')
            subplot.set_title("(" + r'$\sigma$, ' + r'$\beta$, ' + r'$\rho$)=' + "(" + str(sigma) + ", " + beta + ", " + str(rho) + ")")


        self.canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(self.canvas, self.root)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, self.canvas, toolbar)

        self.canvas.mpl_connect("key_press_event", on_key_press)

        self.txt_N = tkinter.StringVar()
        self.txt_dt = tkinter.StringVar()
        self.txt_x = tkinter.StringVar()
        self.txt_y = tkinter.StringVar()
        self.txt_z = tkinter.StringVar()

        self.txt_N.set("N = " + str(self.range_N[0]))
        self.txt_dt.set("dt = " + str(round(self.range_dt[0],4)))
        self.txt_x.set("x = " + str(np.round(self.range_initial_x[0],3)))
        self.txt_y.set("y = " + str(np.round(self.range_initial_y[0],3)))
        self.txt_z.set("z = " + str(np.round(self.range_initial_z[0],3)))

        self.scaler_dt = tkinter.Scale(master=self.root, from_=1, to=100, orient=tkinter.HORIZONTAL, width = 20, command = self.update_sc_dt, bg='#BFBFBF')
        self.scaler_N = tkinter.Scale(master=self.root, from_=1, to=100, orient=tkinter.HORIZONTAL, width = 20, command = self.update_sc_N, bg='#E3BA7C')
        

        label_N = tkinter.Label(textvariable = self.txt_N, width = 14, bg='#E3BA7C')
        label_dt = tkinter.Label(textvariable = self.txt_dt, width = 14, bg='#BFBFBF')
        label_x = tkinter.Label(textvariable = self.txt_x, width = 14, bg='#D02A1E')
        label_y = tkinter.Label(textvariable = self.txt_y, width = 14, bg='#00C753')
        label_z = tkinter.Label(textvariable = self.txt_z, width = 14, bg='#0CB1F2')
        self.scaler_2 = tkinter.Scale(master=self.root, from_=1, to=100, orient=tkinter.HORIZONTAL, width = 20, command = self.update_scx, bg='#D02A1E')
        self.scaler_3 = tkinter.Scale(master=self.root, from_=1, to=100, orient=tkinter.HORIZONTAL, width = 20, command = self.update_scy, bg='#00C753')
        self.scaler_4 = tkinter.Scale(master=self.root, from_=1, to=100, orient=tkinter.HORIZONTAL, width = 20, command = self.update_scz, bg='#0CB1F2')


        self.scaler_N.bind("<ButtonRelease-1>", self.updateValue)
        self.scaler_dt.bind("<ButtonRelease-1>", self.updateValue)

        self.scaler_2.bind("<ButtonRelease-1>", self.updateValue)
        self.scaler_3.bind("<ButtonRelease-1>", self.updateValue)
        self.scaler_4.bind("<ButtonRelease-1>", self.updateValue)

        button = tkinter.Button(master=self.root, text="Save ", command=self._save, width = 14, bg= '#8DA696')

        #self.root.geometry('250x200+250+200')
        location_x = 910
        location_y = 384
        button.place(x=location_x+220, y=location_y+100)

        self.scaler_N.place(x=location_x, y=location_y+100)
        label_N.place(x=location_x, y=location_y+80)

        self.scaler_dt.place(x=location_x+110, y=location_y+100)
        label_dt.place(x=location_x + 110, y=location_y+80)

        self.scaler_2.place(x=location_x, y=location_y + 20)
        label_x.place(x=location_x, y=location_y)

        self.scaler_3.place(x=location_x+110, y=location_y + 20)
        label_y.place(x=location_x+110, y=location_y)

        self.scaler_4.place(x=location_x+220, y=location_y+20)
        label_z.place(x=location_x + 220, y=location_y)

        self.updateValue('event')

    def run_gui(self):
        
        self.root.mainloop()

    def destroy_gui(self):
        self.root.destroy()
        return True

    def update_sc_N(self, event):
        self.txt_N.set("N: = " + str(self.range_N[int(event)-1]))

    def update_sc_dt(self, event):
        self.txt_dt.set("dt: = " + str(round(self.range_dt[int(event)-1],4)))        

    def update_scx(self, event):
        self.txt_x.set("x = " + str(np.round(self.range_initial_x[int(event)], 3)))

    def update_scy(self, event):
        self.txt_y.set("y = " + str(np.round(self.range_initial_y[int(event)], 3)))

    def update_scz(self, event):
        self.txt_z.set("z = " + str(np.round(self.range_initial_z[int(event)], 3)))



    def updateValue(self, event):

        value_N = int(self.scaler_N.get()) - 1
        value_dt = int(self.scaler_dt.get()) -1
        value_2 = int(self.scaler_2.get()) - 1
        value_3 = int(self.scaler_3.get()) - 1
        value_4 = int(self.scaler_4.get()) - 1

        self.experiment_data = {}
        self.experiment_data["init_x"] = self.range_initial_x[value_2]
        self.experiment_data["init_y"] = self.range_initial_y[value_3]
        self.experiment_data["init_z"] = self.range_initial_z[value_4]
        self.experiment_data["dt"] = self.range_dt[value_dt]
        self.experiment_data["N"] = self.range_N[value_N]
        self.experiment_data["beta"] = self.list_beta
        self.experiment_data["sigma"] = self.list_sigma
        self.experiment_data["rho"] = self.list_rho
        self.experiment_data["data"] = []
        time_start = timeit.default_timer()
        for (sig, r, bet) in zip(self.list_sigma, self.list_rho, self.list_beta):

            x_start = [self.range_initial_x[value_2]]; y_start = [self.range_initial_y[value_3]]; z_start = [self.range_initial_z[value_4]]
            sampling_start_time = timeit.default_timer()
            x_sampled, y_sampled, z_sampled = euler(x_start, y_start, z_start, sig, bet, r, self.range_dt[value_dt], self.range_N[value_N])
            sampling_time = timeit.default_timer() - sampling_start_time
            self.experiment_data["data"].append([x_sampled, y_sampled, z_sampled, sampling_time])

        self.experiment_data["elapsed_time"] = timeit.default_timer() - time_start

        for (subplot, data_set, bstr, sig, r) in zip(self.subplots, self.experiment_data["data"], self.list_beta_string, self.list_sigma, self.list_rho):
            subplot.clear()    
            subplot.plot(data_set[0], data_set[1], data_set[2], lw=0.5)
            subplot.set_xlabel('x')
            subplot.set_ylabel('y')
            subplot.set_zlabel('z')
            subplot.set_title("(" + r'$\sigma$, ' + r'$\beta$, ' + r'$\rho$)=' + "(" + str(sig) + ", " + bstr + ", " + str(r) + ")")
    
        #subplot_2.plot(t, value * np.sin(value * np.pi * t))
        self.canvas.draw()



    def _save(self):
        
        if self.file_address is None or len(self.file_address) == 0:
            self.file_address = tkinter.filedialog.askdirectory()
            if "LoratResults" not in self.file_address and len(self.file_address):
                self.file_address = os.path.join(self.file_address, "LoratResults")
                if not os.path.exists(self.file_address):
                    os.makedirs(self.file_address)

        if len(self.file_address):

            experiment_name = ';'.join([
                "N=" + str(self.experiment_data["N"]),
                "dt=" + str(round(self.experiment_data["dt"], 3)),
                "x=" + str(round(self.experiment_data["init_x"], 3)),
                "y=" + str(round(self.experiment_data["init_y"], 3)),
                "z=" + str(round(self.experiment_data["init_z"], 3))
            ])

            #experiment_name = str(uuid.uuid1())[:16]
            experiment_address = os.path.join(self.file_address, experiment_name)
            if not os.path.exists(experiment_address):
                os.makedirs(experiment_address)
            
            np.save(os.path.join(experiment_address, experiment_name + ".npy"), self.experiment_data)
            generate_pdf(os.path.join(experiment_address, "gendata" + ".pdf"), self.experiment_data["init_x"], self.experiment_data["init_y"], self.experiment_data["init_z"], self.experiment_data["N"], self.experiment_data["dt"], self.experiment_data["elapsed_time"])
            f = open(os.path.join(experiment_address, experiment_name + ".csv"), 'w', newline="")
            csvw = csv.writer(f, delimiter=",")
            csvw.writerow(["init x", "init y", "init z", "N", "dt", "elapsed_time_total"])
            csvw.writerow([self.experiment_data["init_x"], self.experiment_data["init_y"], self.experiment_data["init_z"], self.experiment_data["N"], self.experiment_data["dt"], self.experiment_data["elapsed_time"]])
            for (data_set, sigma, beta, rho, beta_string) in zip(self.experiment_data["data"], self.list_sigma, self.list_beta, self.list_rho, self.list_beta_string):
                csvw.writerow(["beta", "sigma", "rho", "time_elapsed"])
                csvw.writerow([sigma, beta, rho, data_set[3]])
                csvw.writerow(["x", "y", "z"])
                graph_name = ';'.join([experiment_name,
                    "S=" + str(round(beta, 3)),
                    "B=" + str(round(sigma, 3)),
                    "R=" + str(round(rho, 3))
                ])
                graph(data_set[0], data_set[1], data_set[2], self.experiment_data["dt"], int(self.experiment_data["N"]), sigma, beta_string, rho, data_set[3], os.path.join(experiment_address, graph_name + ".png"))
                graph(data_set[0], data_set[1], data_set[2], self.experiment_data["dt"], int(self.experiment_data["N"]), sigma, beta_string, rho, data_set[3], os.path.join(experiment_address, graph_name + ".pdf"))
                for (x, y, z) in zip(data_set[0], data_set[1], data_set[2]):
                    csvw.writerow([x, y, z])
            f.close()

            merge_pdfs(experiment_address, experiment_name)