import tkinter
import lorenz

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

font = {'family' : 'Arial',
        'size' : '11'}

N = np.linspace(start = 500, stop = 50000, num = 100, dtype = int)
dt = np.linspace(start = 0.01, stop = 0.0001, num = 100)
x = np.linspace(start = 0, stop = 10, num = 100)
y = np.linspace(start = 0, stop = 10, num = 100)
z = np.linspace(start = 0, stop = 10, num = 100)
root = tkinter.Tk()
root.wm_title("Embedding in Tk")
sigma = [10, 10, 10, 14, 14]
betta = [8/3, 8/3, 8/3, 8/3, 13/3]
beta_str = ["8/3", "8/3", "8/3", "8/3", "13/3"] #generate string to be able to show ratio
ro = [6, 16, 28, 28, 28]

fig = Figure(figsize=(10, 5), dpi=100)
t = np.arange(0, 3, .01)
subplots = []

subplots.append(fig.add_subplot(3, 2, 1, projection = '3d'))
subplots.append(fig.add_subplot(3, 2, 2, projection = '3d'))
subplots.append(fig.add_subplot(3, 2, 3, projection = '3d'))
subplots.append(fig.add_subplot(3, 2, 4, projection = '3d'))
subplots.append(fig.add_subplot(3, 2, 5, projection = '3d'))

for (subplot, index_s, index_b, index_r) in zip(subplots, sigma, beta_str, ro):
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


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate



button = tkinter.Button(master=root, text="Quit", command=_quit, width = 20)
scaler = tkinter.Scale(master=root, from_=0, to=100, orient=tkinter.HORIZONTAL, width = 20)
txt = tkinter.StringVar()
txt.set('dt')
label = tkinter.Label(textvariable = txt)
scaler_2 = tkinter.Scale(master=root, from_=0, to=100, orient=tkinter.HORIZONTAL, width = 20)
scaler_3 = tkinter.Scale(master=root, from_=0, to=100, orient=tkinter.HORIZONTAL, width = 20)
scaler_4 = tkinter.Scale(master=root, from_=0, to=100, orient=tkinter.HORIZONTAL, width = 20)

def updateValue(event):
    value = int(scaler.get())
    value_2 = int(scaler_2.get())
    value_3 = int(scaler_3.get())
    value_4 = int(scaler_4.get())

    print("dt: = ", dt[value], "    N: = ", N[value],   "  x: = ", x[value_2], "   y= :  ", y[value_3],  "z=  :    ", z[value_4])
    txt.set("dt: = " + str(round(dt[value],4)) + "    N: = " + str(N[value]))
    for (subplot, sig, r, bet, bstr) in zip(subplots, sigma, ro, betta, beta_str):

        x_start = [x[value_2]]; y_start = [y[value_3]]; z_start = [z[value_4]]
        s, t, u = lorenz.euler(x_start, y_start, z_start, sig, r, bet, dt[value], N[value])
        subplot.clear()    
        subplot.plot(s, t, u, lw=0.5)
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

button.pack(padx = 130, side=tkinter.LEFT)
label.pack(side = tkinter.LEFT)
scaler.pack(side=tkinter.LEFT)
scaler_2.pack(padx = 50, side=tkinter.RIGHT)
scaler_3.pack(padx = 50, side=tkinter.RIGHT)
scaler_4.pack(padx = 50, side=tkinter.RIGHT)
tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.