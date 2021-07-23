import tkinter
import lorenz

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

N = np.linspace(start = 500, stop = 50000, num = 100, dtype = int)
dt = np.linspace(start = 0.01, stop = 0.0001, num = 100)
x = np.linspace(start = 0.1, stop = 1000, num = 100)
y = np.linspace(start = 0.00001, stop = 1, num = 100)
z = np.linspace(start = 0.001, stop = 10, num = 100)
root = tkinter.Tk()
root.wm_title("Embedding in Tk")
sigma = [10, 10, 10, 14, 14]
betta = [8/3, 8/3, 8/3, 8/3, 13/3]
ro = [6, 16, 28, 28, 28]
fig = Figure(figsize=(15, 10), dpi=100)
t = np.arange(0, 3, .01)
subplots = []
subplots.append(fig.add_subplot(3, 2, 1, projection = '3d'))
subplots.append(fig.add_subplot(3, 2, 2, projection = '3d'))
subplots.append(fig.add_subplot(3, 2, 3, projection = '3d'))
subplots.append(fig.add_subplot(3, 2, 4, projection = '3d'))
subplots.append(fig.add_subplot(3, 2, 5, projection = '3d'))



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


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate



button = tkinter.Button(master=root, text="Quit", command=_quit)
scaler = tkinter.Scale(master=root, from_=0, to=100, orient=tkinter.HORIZONTAL)
scaler_2 = tkinter.Scale(master=root, from_=0, to=100, orient=tkinter.HORIZONTAL)
scaler_3 = tkinter.Scale(master=root, from_=0, to=100, orient=tkinter.HORIZONTAL)
scaler_4 = tkinter.Scale(master=root, from_=0, to=100, orient=tkinter.HORIZONTAL)
scaler_5 = tkinter.Scale(master=root, from_=0, to=100, orient=tkinter.HORIZONTAL)

def updateValue(event):
    value = int(scaler.get())
    value_2 = int(scaler_2.get())
    value_3 = int(scaler_3.get())
    value_4 = int(scaler_4.get())
    value_5 = int(scaler_5.get())

    print("dt: = ", dt[value], "    N: = ", N[value_2],   "  x: = ", x[value_3], "   y= :  ", y[value_4],  "z=  :    ", z[value_5])
    for (subplot, sig, r, bet) in zip(subplots, sigma, ro, betta):

        x_start = [x[value_3]]; y_start = [y[value_4]]; z_start = [z[value_5]]
        s, t, u = lorenz.euler(x_start, y_start, z_start, sig, r, bet, dt[value], N[value_2])
        subplot.clear()    
    
        subplot.plot(s, t, u, lw=0.5)
    #subplot_2.plot(t, value * np.sin(value * np.pi * t))
    canvas.draw()
    

scaler.bind("<ButtonRelease-1>", updateValue)
scaler_2.bind("<ButtonRelease-1>", updateValue)
scaler_3.bind("<ButtonRelease-1>", updateValue)
scaler_4.bind("<ButtonRelease-1>", updateValue)
scaler_5.bind("<ButtonRelease-1>", updateValue)

button.pack(side=tkinter.BOTTOM)
scaler.pack(side=tkinter.BOTTOM)
scaler_2.pack(side=tkinter.BOTTOM)
scaler_3.pack(side=tkinter.BOTTOM)
scaler_4.pack(side=tkinter.BOTTOM)
scaler_5.pack(side=tkinter.BOTTOM)
tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.