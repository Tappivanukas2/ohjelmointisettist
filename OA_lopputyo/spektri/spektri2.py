#Tatu Lehtola
#xdata on numpy array

import os
import ikkunasto as ik
import numpy as np
import matplotlib.pyplot as plt
import kuvaajat
import plotly.graph_objs as go
import plotly.tools as tools
import plotly.figure_factory as ff
import scipy
import peakutils
import math

elementit = {
    "tekstilaatikko": "Luettiin {rivit} tiedostoa.",
    "virheviesti": "Ei sopivaa dataa luettavaksi",
    "piirtoalue": None,
    "kuvaaja": None,
    "piirtoalue.old_coords": None,
    "xpisteet": [],
    "ypisteet": [],
    "kehys1": None,
    "kehys2": None,
    "ikkuna": None,
    "laatikko1": None,
    "laatikko2": None,
    "xdata": [],
    "ydata": [],
    "click": 0
}


def poista_lineaarinen_tausta():
    """
    Poistaa lineaarisen taustan kuvaajasta.
    https://peakutils.readthedocs.io/en/latest/tutorial_a.html#estimating-and-removing-the-baseline
    """
    try:
        elementit["ax"].cla()
        y = elementit["ydata"]
        x = elementit["xdata"]
        y2 = y + np.polyval([0.002,-0.08,5], x)
        base = peakutils.baseline(y2, 2)
        elementit["ax"].set_xlabel("Binding energy(eV)")
        elementit["ax"].set_ylabel("Intensity (arbitary units")
        elementit["ax"].plot(x, y-base)
        elementit["piirtoalue"].draw()
    except ValueError:
        ik.kirjoita_tekstilaatikkoon(elementit["laatikko1"],
        elementit["virheviesti"], tyhjaa=False)
        return


    """
    try:
        elementit["ax"].cla()
        y = elementit["ydata"]
        x = elementit["xdata"]
        y2 = y + np.polyval([0.002,-0.08,5], x)
        base = peakutils.baseline(y2, 2)
        elementit["ax"].set_xlabel("Binding energy(eV)")
        elementit["ax"].set_ylabel("Intensity (arbitary units")
        elementit["ax"].plot(x, y-base)
        elementit["piirtoalue"].draw()
    except ValueError:
        ik.kirjoita_tekstilaatikkoon(elementit["laatikko1"],
        elementit["virheviesti"], tyhjaa=False)
        return
    """


def lue_data(path):
    """
    Lukee kaikki tiedostot annetusta kansiosta. Ohittaa tiedostot, jotka eivät
    ole päätteeltään .txt.
    """
    x = []
    y = []
    files = []
    try:
        for file in os.listdir(path): #lukee kansion
            if file.endswith(".txt"):    #tarkastaa tiedostopäätteet
                files.append(file)
                with open(os.path.join(path, file)) as kohde:  #avaa tiedoston
                    lines = (line.rstrip() for line in kohde)
                    lines = list(line for line in lines if line)
                    file_len = len(lines)
                    try:
                        for i in range(file_len): #vaihtaa listan alkioden muodon stringistä float
                            ass = lines[i]
                            ass.strip()
                            lista = ass.split(" ")
                            ekafloat = float(lista[0])
                            tokafloat = float(lista[1])
                            x.append(ekafloat)
                            y.append(tokafloat)
                    except ValueError:
                        pass
                    x1 = sum(x)/len(x)
                    #y1 = sum(y)
                    elementit["xdata"].append(x1)
                    elementit["ydata"].append(y)
            else:
                continue
    except FileNotFoundError:
        return
    return files


def valitse_datapiste(event):
    """
    Ottaa vastaan hiiren klikkaustapahtuman ja lukee siitä datapisteen x- ja
    y-arvot sekä sovittaa pisteiden väliin suoran :_D.
    """
    elementit["xpisteet"].append(event.xdata)
    elementit["ypisteet"].append(event.ydata)
    elementit["ax"].plot(elementit["xpisteet"][-2:], elementit["ypisteet"][-2:], "-r")
    elementit["piirtoalue"].draw()

def avaa_kansio():
    """
    Napinkäsittelijä, joka pyytää käyttäjää valitsemaan kansion avaamalla
    kansioselaimen. Lataa datan valitusta kansiosta ja ilmoittaa käyttöliittymän
    tekstilaatikkoon montako tiedostoa luettiin.
    """
    path = ik.avaa_hakemistoikkuna("Valitse kansio")
    try:
        files = lue_data(path)
    except TypeError:
        return
    try:
        file_number = len(files)
    except TypeError:
        ik.kirjoita_tekstilaatikkoon(elementit["laatikko1"],
        elementit["virheviesti"], tyhjaa=False)
        return
    if file_number > 0:
        ik.kirjoita_tekstilaatikkoon(elementit["laatikko1"],
        elementit["tekstilaatikko"].format(rivit=file_number), tyhjaa=False)
    else:
        ik.kirjoita_tekstilaatikkoon(elementit["laatikko1"],
        elementit["virheviesti"], tyhjaa=False)
        return

def piirra_kuvaaja():
    """
    Piirtää kuvaajan :D
    """
    try:
        if elementit["xdata"] and elementit["ydata"]:
            elementit["ax"].cla()
            elementit["ax"].plot(elementit["xdata"], elementit["ydata"])
            elementit["ax"].set_xlabel("Binding energy(eV)")
            elementit["ax"].set_ylabel("Intensity (arbitary units")
            elementit["piirtoalue"].draw()
        else:
            ik.kirjoita_tekstilaatikkoon(elementit["laatikko1"],
            elementit["virheviesti"], tyhjaa=False)
    except ValueError:
        return

def tallennus():
    polku = ik.avaa_tallennusikkuna("Tallenna kuvaaja")
    plt.savefig(polku)

def laske_intensiteetti():
    try:
        x0 = elementit["xpisteet"][-2]; x1 = elementit["xpisteet"][-1]
        y0 = elementit["ypisteet"][-2]; y1 = elementit["ypisteet"][-1]
        xpoints = x0, x1
        ypoints = y0, y1
        integraali = round(np.trapz(elementit["ydata"], xpoints))
        ik.kirjoita_tekstilaatikkoon(elementit["laatikko1"],
        "Piikin intensiteetti on: {}".format(integraali))
    except IndexError:
        return

def main():
    """
    Luo käyttöliittymän, jossa on klikattava kuvaaja, tekstilaatikko sekä napit.
    """
    elementit["ikkuna"] = ik.luo_ikkuna("liittymä")
    elementit["kehys1"] = ik.luo_kehys(elementit["ikkuna"], ik.VASEN)
    elementit["kehys2"] = ik.luo_kehys(elementit["ikkuna"], ik.VASEN)
    elementit["laatikko1"] = ik.luo_tekstilaatikko(elementit["kehys2"], leveys=30, korkeus=30)
    elementit["piirtoalue"], elementit["kuvaaja"] = ik.luo_kuvaaja(elementit["laatikko2"],
    valitse_datapiste, 800, 400)
    elementit["ax"] = elementit["kuvaaja"].add_subplot(111)
    ik.luo_nappi(elementit["kehys1"], "lataa", avaa_kansio)
    ik.luo_nappi(elementit["kehys1"], "tallenna kuvaaja", tallennus)
    ik.luo_nappi(elementit["kehys1"], "piirra kuvaaja", piirra_kuvaaja)
    ik.luo_nappi(elementit["kehys1"], "laske intensiteetti", laske_intensiteetti)
    ik.luo_nappi(elementit["kehys1"], "poista lineaarinen tausta", poista_lineaarinen_tausta)
    ik.luo_nappi(elementit["kehys1"], "quit", ik.lopeta)
    ik.kaynnista()

if __name__ == "__main__":
    main()