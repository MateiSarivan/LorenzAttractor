import os
import tkinter
import lorenz
import timeit
import csv

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from plotting import graph
import numpy as np
import json
import fractions
from pdf_gen import generate_pdf
from pdf_merge import merge_pdfs

font = {'family' : 'Arial',
        'size' : '11'}

f = open('configuration.json',)
data = json.load(f)

file_address = None
experiment_data = {}

N = np.linspace(start = data['configuration']['N']['min'], stop = data['configuration']['N']['max'], num = 100, dtype = int)
dt = np.linspace(start = data['configuration']['dt']['max'], stop = data['configuration']['dt']['min'], num = 100)
x = np.linspace(start = data['configuration']['x']['min'], stop = data['configuration']['x']['max'], num = 100)
y = np.linspace(start = data['configuration']['y']['min'], stop = data['configuration']['y']['max'], num = 100)
z = np.linspace(start = data['configuration']['z']['min'], stop = data['configuration']['z']['max'], num = 100)

root = tkinter.Tk()
root.geometry("1366x768")
root.wm_title("Embedding in Tk")
sigma = np.float_(data['configuration']['sigma'])
beta = [float(fractions.Fraction(x)) for x in data['configuration']['beta']] #transform beta to float
beta_str = data['configuration']['beta']
rho = np.float_(data['configuration']['rho'])

fig = Figure(figsize=(10, 5), dpi=100)
t = np.arange(0, 3, .01)
subplots = []

subplots.append(fig.add_subplot(2, 3, 1, projection = '3d'))
subplots.append(fig.add_subplot(2, 3, 2, projection = '3d'))
subplots.append(fig.add_subplot(2, 3, 3, projection = '3d'))
subplots.append(fig.add_subplot(2, 3, 4, projection = '3d'))
subplots.append(fig.add_subplot(2, 3, 5, projection = '3d'))

for (subplot, index_s, index_b, index_r) in zip(subplots, sigma, beta_str, rho):
    subplot.set_xlabel('x')
    subplot.set_ylabel('y')
    subplot.set_zlabel('z')
    subplot.set_title("(" + r'$\sigma$, ' + r'$\beta$, ' + r'$\rho$)=' + "(" + str(index_s) + ", " + index_b + ", " + str(index_r) + ")")

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)




txt = tkinter.StringVar()
txt_x = tkinter.StringVar()
txt_y = tkinter.StringVar()
txt_z = tkinter.StringVar()

txt.set("dt = " + str(round(dt[0],4)) + "    N = " + str(N[0]))
txt_x.set("x = " + str(np.round(x[0],3)))
txt_y.set("y = " + str(np.round(y[0],3)))
txt_z.set("z = " + str(np.round(z[0],3)))

def update_sc(event):
    print(event)
    txt.set("dt: = " + str(round(dt[int(event)-1],4)) + "    N: = " + str(N[int(event)-1]))

def update_scx(event):
    print(event)
    txt_x.set("x = " + str(np.round(x[int(event)], 3)))

def update_scy(event):
    print(event)
    txt_y.set("y = " + str(np.round(y[int(event)], 3)))

def update_scz(event):
    print(event)
    txt_z.set("z = " + str(np.round(z[int(event)], 3)))


scaler = tkinter.Scale(master=root, from_=1, to=100, orient=tkinter.HORIZONTAL, width = 20, command = update_sc, bg='#E3BA7C')


label = tkinter.Label(textvariable = txt, width = 25, bg='#E3BA7C')
label_x = tkinter.Label(textvariable = txt_x, width = 14, bg='#D02A1E')
label_y = tkinter.Label(textvariable = txt_y, width = 14, bg='#00C753')
label_z = tkinter.Label(textvariable = txt_z, width = 14, bg='#0CB1F2')
scaler_2 = tkinter.Scale(master=root, from_=1, to=100, orient=tkinter.HORIZONTAL, width = 20, command = update_scx, bg='#D02A1E')
scaler_3 = tkinter.Scale(master=root, from_=1, to=100, orient=tkinter.HORIZONTAL, width = 20, command = update_scy, bg='#00C753')
scaler_4 = tkinter.Scale(master=root, from_=1, to=100, orient=tkinter.HORIZONTAL, width = 20, command = update_scz, bg='#0CB1F2')



def updateValue(event):
    global experiment_data
    value = int(scaler.get()) - 1
    value_2 = int(scaler_2.get()) - 1
    value_3 = int(scaler_3.get()) - 1
    value_4 = int(scaler_4.get()) - 1

    print("dt: = ", dt[value], "    N: = ", N[value],   "  x: = ", x[value_2], "   y= :  ", y[value_3],  "z=  :    ", z[value_4])
    experiment_data = {}
    experiment_data["init_x"] = x[value_2]
    experiment_data["init_y"] = y[value_3]
    experiment_data["init_z"] = z[value_4]
    experiment_data["dt"] = dt[value]
    experiment_data["N"] = N[value]
    
    experiment_data["data"] = []
    time_start = timeit.default_timer()
    for (sig, r, bet) in zip(sigma, rho, beta):

        x_start = [x[value_2]]; y_start = [y[value_3]]; z_start = [z[value_4]]
        sampling_start_time = timeit.default_timer()
        x_sampled, y_sampled, z_sampled = lorenz.euler(x_start, y_start, z_start, sig, bet, r, dt[value], N[value])
        sampling_time = timeit.default_timer() - sampling_start_time
        experiment_data["data"].append([x_sampled, y_sampled, z_sampled, sampling_time])

    experiment_data["elapsed_time"] = timeit.default_timer() - time_start

    for (subplot, data_set, bstr, sig, r) in zip(subplots, experiment_data["data"], beta_str, sigma, rho):
        subplot.clear()    
        subplot.plot(data_set[0], data_set[1], data_set[2], lw=0.5)
        subplot.set_xlabel('x')
        subplot.set_ylabel('y')
        subplot.set_zlabel('z')
        subplot.set_title("(" + r'$\sigma$, ' + r'$\beta$, ' + r'$\rho$)=' + "(" + str(sig) + ", " + bstr + ", " + str(r) + ")")
 
     #subplot_2.plot(t, value * np.sin(value * np.pi * t))
    canvas.draw()
    

scaler.bind("<ButtonRelease-1>", updateValue)
scaler_2.bind("<ButtonRelease-1>", updateValue)
scaler_3.bind("<ButtonRelease-1>", updateValue)
scaler_4.bind("<ButtonRelease-1>", updateValue)
def _save():
    global file_address, experiment_data
    #print(total_time)
    print(file_address)
    if file_address is None:
        file_address = tkinter.filedialog.askdirectory()
        if "LoratResults" not in file_address:
            file_address = os.path.join(file_address, "LoratResults")
            if not os.path.exists(file_address):
                os.makedirs(file_address)
            

    experiment_name = ';'.join([
        "N&dt=" + str(scaler.get()),
        "x=" + str(scaler_2.get()),
        "y=" + str(scaler_3.get()),
        "z=" + str(scaler_3.get())
    ])
    experiment_address = os.path.join(file_address, experiment_name)
    if not os.path.exists(experiment_address):
        os.makedirs(experiment_address)
    
    np.save(os.path.join(experiment_address, experiment_name + ".npy"), experiment_data)
    generate_pdf(os.path.join(experiment_address, "gendata" + ".pdf"), experiment_data["init_x"], experiment_data["init_y"], experiment_data["init_z"], experiment_data["N"], experiment_data["dt"], experiment_data["elapsed_time"])
    f = open(os.path.join(experiment_address, experiment_name + ".csv"), 'w', newline="")
    csvw = csv.writer(f, delimiter=",")
    csvw.writerow(["init x", "init y", "init z", "N", "dt", "elapsed_time_total"])
    csvw.writerow([experiment_data["init_x"], experiment_data["init_y"], experiment_data["init_z"], experiment_data["N"], experiment_data["dt"], experiment_data["elapsed_time"]])
    i = 0
    for (data_set, s, b, r, bs) in zip(experiment_data["data"], sigma, beta, rho, beta_str):
        csvw.writerow(["beta", "sigma", "rho", "time_elapsed"])
        csvw.writerow([s, b, r, data_set[3]])
        csvw.writerow(["x", "y", "z"])
        graph_name = ';'.join([experiment_name,
            "S=" + str(i),
            "B=" + str(i),
            "R=" + str(i)
        ])
        i += 1
        graph(data_set[0], data_set[1], data_set[2], experiment_data["dt"], int(experiment_data["N"]), s, bs, r, data_set[3], os.path.join(experiment_address, graph_name + ".png"))
        graph(data_set[0], data_set[1], data_set[2], experiment_data["dt"], int(experiment_data["N"]), s, bs, r, data_set[3], os.path.join(experiment_address, graph_name + ".pdf"))
        for (x, y, z) in zip(data_set[0], data_set[1], data_set[2]):
            csvw.writerow([x, y, z])
    f.close()

    merge_pdfs(experiment_address, experiment_name)
    



    


button = tkinter.Button(master=root, text="Save ", command=_save, width = 20, bg= '#8DA696')

#root.geometry('250x200+250+200')
button.place(x=1550, y=750)

scaler.place(x=1320, y=800)
label.place(x=1275, y=750)

scaler_2.place(x=1250, y=650)
label_x.place(x=1250, y=600)

scaler_3.place(x=1450, y=650)
label_y.place(x=1450, y=600)

scaler_4.place(x=1650, y=650)
label_z.place(x=1650, y=600)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.