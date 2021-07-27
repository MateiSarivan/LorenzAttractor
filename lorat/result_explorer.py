from tkinter import *
import tkinter.filedialog
import os
import numpy as np
from plotting import graph



file_address = None
experiment = {}
  
# Creating the root window
root = tkinter.Tk()
root.geometry("450x300")

  
# Creating a Listbox and
# attaching it to root window

frame_1 = Frame(root)
frame_2 = Frame(root)
frame_3 = Frame(frame_2)

txt_x_initial = tkinter.StringVar()
txt_y_initial = tkinter.StringVar()
txt_z_initial = tkinter.StringVar()
txt_dt = tkinter.StringVar()
txt_N = tkinter.StringVar()
listbox_2 = Listbox(frame_3, height=5, width=25)
scrollbar_2 = Scrollbar(frame_3)
scrollbar_2.pack(side = LEFT, fill = BOTH)
listbox_2.config(yscrollcommand = scrollbar_2.set)
scrollbar_2.config(command = listbox_2.yview)
def list_select(event):
    global file_address, experiment
    data = None
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
    if data is not None:
        listbox_2.delete(0, END)
        experiment_address = os.path.join(file_address, data, data + ".npy")
        print(experiment_address)
        experiment_data = np.load(experiment_address, allow_pickle=True)
        txt_x_initial.set("Initial x: " + str(experiment_data.item().get("init_x")))
        experiment["x"] = experiment_data.item().get("init_x")
        txt_y_initial.set("Initial y: " + str(experiment_data.item().get("init_y")))
        experiment["y"] = experiment_data.item().get("init_y")
        txt_z_initial.set("Initial z: " + str(experiment_data.item().get("init_z")))
        experiment["z"] = experiment_data.item().get("init_z")
        txt_dt.set("dt: " + str(experiment_data.item().get("dt")))
        experiment["dt"] = experiment_data.item().get("dt")
        txt_N.set("N: " + str(experiment_data.item().get("N")))
        experiment["N"] = experiment_data.item().get("N")
        beta_parameters = experiment_data.item().get("beta")
        experiment["beta"] = beta_parameters
        sigma_parameters = experiment_data.item().get("sigma")
        experiment["sigma"] = sigma_parameters
        rho_parameters = experiment_data.item().get("rho")
        experiment["rho"] = rho_parameters
        experiment["data"] = experiment_data.item().get("data")
        print(beta_parameters)

        for (sigma, beta, rho) in zip(sigma_parameters, beta_parameters, rho_parameters):
            listbox_2.insert(END, "σ=" + str(np.round(sigma, 3)) + ";  β=" + str(np.round(beta, 3)) + ";  ρ=" + str(rho))


def list_select_2(event):
    global experiment
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        print(index)
        experiment["index_constants"] = index
        

listbox = Listbox(frame_1, width = 35)
listbox.bind("<<ListboxSelect>>", list_select)
listbox_2.bind("<<ListboxSelect>>", list_select_2)
# Adding Listbox to the left
# side of root window


label_x_initial = tkinter.Label(master=frame_2, textvariable = txt_x_initial, width = 25, bg='#E3BA7C')
label_y_initial = tkinter.Label(master=frame_2, textvariable = txt_y_initial, width = 25, bg='#E3BA7C')
label_z_initial = tkinter.Label(master=frame_2, textvariable = txt_z_initial, width = 25, bg='#E3BA7C')
label_dt = tkinter.Label(master=frame_2, textvariable = txt_dt, width = 25, bg='#E3BA7C')
label_N = tkinter.Label(master=frame_2, textvariable = txt_N, width = 25, bg='#E3BA7C')

listbox_2.pack(side=TOP, fill="y", expand=True)

label_x_initial.pack()
label_y_initial.pack()
label_z_initial.pack()
label_dt.pack()
label_N.pack()
frame_3.pack()
def _plot():
    index = experiment["index_constants"]
    xyz = experiment["data"][index]
    graph(xyz[0], xyz[1], xyz[2], experiment["dt"], experiment["N"], experiment["sigma"][index], experiment["beta"][index], experiment["rho"][index], xyz[3])

button = tkinter.Button(master=frame_2, text="Plot", command=_plot, width = 20, bg= '#8DA696')
button.pack()

frame_2.pack(side = RIGHT, fill="x", expand=True)


listbox.pack(side = RIGHT, fill = BOTH)
  
# Creating a Scrollbar and 
# attaching it to root window
scrollbar = Scrollbar(frame_1)
  
# Adding Scrollbar to the right
# side of root window
scrollbar.pack(side = LEFT, fill = BOTH)
  
# Insert elements into the listbox
      
# Attaching Listbox to Scrollbar
# Since we need to have a vertical 
# scroll we use yscrollcommand
listbox.config(yscrollcommand = scrollbar.set)
  
# setting scrollbar command parameter 
# to listbox.yview method its yview because
# we need to have a vertical view
scrollbar.config(command = listbox.yview)

frame_1.pack(side = LEFT, fill="y")


def get_address():
    global file_address

    file_address = tkinter.filedialog.askdirectory()
    if "LoratResults" not in file_address:

        root.quit()
    else:
        experiments_names = os.listdir(file_address)
        for experiment_name in experiments_names:
            listbox.insert(tkinter.END, experiment_name)


root.after(100, get_address)
root.mainloop()