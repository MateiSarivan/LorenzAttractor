import os
from reportlab.lib.colors import blue, black
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas
import datetime
import time
import psutil
import platform as pfm
import json

def ord(n):
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))

def generate_pdf(file_address, x_0, y_0, z_0, N, dt, elapsed_time):
    """
    pdf generator

    Parameters
    -------
    
    file_address : Path
        Directory for file creation
    x_0 : List of float
        Initial value of x.
    y_0 : List of float
        Initial value of y.
    z_0 : List of float
        Initial value of z.
    dt: Float
        Iteration step.
    N: Float
        Length of iteration.
    elapsed_time : Float
        Time elapsed for parametric analysis
    """
    
    canvas = Canvas(file_address, pagesize=A4)
    canvas.setFont("Times-Roman", 28)
    canvas.drawString(5 * cm, 27 * cm, "Lorenz Attractor Experiment")
    canvas.setFont("Times-Roman", 20)
    canvas.drawString(4.8 * cm, 26 * cm, "Parametric study using the Euler approach")
    canvas.setFont("Times-Roman", 14)
    canvas.drawString(2.5 * cm, (27-3.5) * cm, "Experiment conducted on ")
    day_today = datetime.datetime.now().strftime("%A")
    date_today = datetime.datetime.now().strftime("%d")
    month_today = datetime.datetime.now().strftime("%B")
    year_today = datetime.datetime.now().strftime("%Y")
    time_hms = time.strftime('%H:%M:%S')

    time_string = ' '.join([day_today + ',',
        "the " + ord(int(date_today)),
        "of " + month_today,
        year_today + ",",
        "at",
        str(time_hms)    
    ])

    canvas.drawString(7.7 * cm, (27-3.5) * cm, time_string)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    canvas.setFillColor(black)
    json_file = os.path.join(dir_path, 'json', 'configuration.json')
    with open(json_file) as f:
        conf = json.load(f)
        beta = conf['configuration']['beta']
        sigma = conf['configuration']['sigma']
        rho = conf['configuration']['rho']
    canvas.drawString(2.5 * cm, (27-4.5) * cm, "The following parameters were selected for the experiment:")
    canvas.drawString(3.5 * cm, (27-5.5) * cm, "1.  Constants:")
    canvas.drawString(4.5 * cm, (27-6.5) * cm, "?? = " + str(sigma).replace('[', '(').replace(']', ')').replace("'", ''))
    canvas.drawString(4.5 * cm, (27-7.5) * cm, "?? = " + str(beta).replace('[', '(').replace(']', ')').replace("'", ''))
    canvas.drawString(4.5 * cm, (27-8.5) * cm, "?? = " + str(rho).replace('[', '(').replace(']', ')').replace("'", ''))
    canvas.drawString(3.5 * cm, (27-9.5) * cm, "2.  Initial Conditions:")
    canvas.drawString(4.5 * cm, (27-10.5) * cm, "x = " + str(x_0))
    textobject = canvas.beginText(4.75 * cm, (27-10.6) * cm)
    textobject.setFont("Times-Roman", 7)
    textobject.textOut("0")
    canvas.drawText(textobject)
    canvas.setFont("Times-Roman", 14)
    canvas.drawString(4.5 * cm, (27-11.5) * cm, "y = " + str(y_0))
    textobject = canvas.beginText(4.75 * cm, (27-11.6) * cm)
    textobject.setFont("Times-Roman", 7)
    textobject.textOut("0")
    canvas.drawText(textobject)
    canvas.setFont("Times-Roman", 14)
    canvas.drawString(4.5 * cm, (27-12.5) * cm, "z = " + str(z_0))
    textobject = canvas.beginText(4.75 * cm, (27-12.6) * cm)
    textobject.setFont("Times-Roman", 7)
    textobject.textOut("0")
    canvas.drawText(textobject)
    canvas.setFont("Times-Roman", 14)
    canvas.drawString(3.5 * cm, (27-13.5) * cm, "3.  Sampling:")
    canvas.drawString(4.5 * cm, (27-14.5) * cm, "Number of samples: N = " + str(N))
    canvas.drawString(4.5 * cm, (27-15.5) * cm, "Sampling frequency: ??t = " + str(dt))

    canvas.drawString(2.5 * cm, (27-16.5) * cm, "Experiment conducted using a computer with: " )
    canvas.drawString(3.5 * cm, (27-17.5) * cm, "Python version: " + pfm.python_version())
    canvas.drawString(3.5 * cm, (27-18.5) * cm, "Python build: " + pfm.python_build()[1])
    canvas.drawString(3.5 * cm, (27-19.5) * cm, "Operating system: " + pfm.system())
    canvas.drawString(3.5 * cm, (27-20.5) * cm, "Operating platform: " + pfm.platform())
    canvas.drawString(3.5 * cm, (27-21.5) * cm, "Processor: " + pfm.processor())
    total_ram = psutil.virtual_memory().total/10**9
    total_ram = str(round(total_ram, 2)) + " GB"
    canvas.drawString(3.5 * cm, (27-22.5) * cm, "RAM installed: " + total_ram)
    canvas.drawString(2.5 * cm, (27-23.5) * cm, "Total experiment elapsed time: " + str(elapsed_time))
    canvas.drawString(2.5 * cm, (27-24.5) * cm, "For each set of constants, 3D and 2D plots are given below: ")

    canvas.save()