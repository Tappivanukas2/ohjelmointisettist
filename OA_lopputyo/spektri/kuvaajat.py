"""
kuvaajan piirtäjä
"""
import tkinter as tk
from tkinter.ttk import Separator
from tkinter import messagebox, filedialog

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

VASEN = tk.LEFT
OIKEA = tk.RIGHT
YLA = tk.TOP
ALA = tk.BOTTOM



def kuvaaja(kehys, hiiri_kasittelija, leveys, korkeus, xdata, ydata):
    """
    Luo Kuvaajan
    """
    kuvaaja = Figure(figsize=(leveys / 100, korkeus / 100), dpi=100)
    piirtoalue = FigureCanvasTkAgg(kuvaaja, master=kehys)
    #piirtoalue.get_tk_widget().pack_forget()
    piirtoalue.get_tk_widget().pack(side=tk.TOP)
    piirtoalue.mpl_connect("button_press_event", hiiri_kasittelija)
    ax = kuvaaja.add_subplot(111)
    ax.plot(xdata, ydata)
    ax.set_xlabel("Binding energy(eV)")
    ax.set_ylabel("Intensity (arbitary units")
    piirtoalue.draw()
    return piirtoalue, ax

def paivita_kuvaaja(xdata, ydata, ax, piirtoalue):
    """
    päivittää kuvaajan xdata ja ydata listojen arvoilla
    """
    try:
        piirtoalue.get_tk_widget().pack_forget()
    except AttributeError:
        pass
    ax.plot(xdata, ydata)
    piirtoalue.draw()



def sulje_kuvaaja(piirtoalue):
    try:
        piirtoalue.get_tk_widget().pack_forget()
    except AttributeError:
        pass



"""
    kuvaajat.kuvaaja(elementit["laatikko2"], valitse_datapiste,
    800, 400, elementit["xdata"], elementit["ydata"])
    #kuvaajat.paivita_kuvaaja(elementit["xdata"], elementit["ydata"], ax, piirtoalue)
"""