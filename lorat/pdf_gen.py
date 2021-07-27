from reportlab.lib.colors import blue, black
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas
import datetime
import time

def ord(n):
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))

canvas = Canvas("font-colors.pdf", pagesize=A4)

# Set font to Times New Roman with 12-point size
canvas.setFont("Times-Roman", 28)
canvas.drawString(5 * cm, 27 * cm, "Lorenz Attractor Experiment")
canvas.setFont("Times-Roman", 20)
canvas.drawString(4.8 * cm, 26 * cm, "Parametric study using the Euler approach")
# Draw blue text one inch from the left and ten
# inches from the bottom
canvas.setFont("Times-Roman", 14)
canvas.drawString(2.5 * cm, (27-3.5) * cm, "Experiment conducted on ")
canvas.setFillColor(blue)
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

canvas.drawString(8 * cm, (27-3.5) * cm, time_string)

canvas.setFillColor(black)

canvas.drawString(2.5 * cm, (27-4.5) * cm, "The following parameters were selected for the experiment:")
canvas.drawString(3.5 * cm, (27-5.5) * cm, "1.  Constants:")
canvas.drawString(4.5 * cm, (27-6.5) * cm, "σ = " + str(4324))
canvas.drawString(4.5 * cm, (27-6.5) * cm, "β = " + str(4324))
canvas.drawString(4.5 * cm, (27-6.5) * cm, "ρ = " + str(4324))


# Save the PDF file
canvas.save()