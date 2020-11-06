#Tatu Lehtola
#xdata on numpy array

import os
import ikkunasto as ik
import numpy as np
import matplotlib.pyplot as plt
import peakutils

elementit = {
    "tekstilaatikko": "Luettiin {rivit} tiedostoa.",
    "virheviesti": "Ei sopivaa dataa luettavaksi",
    "virheviesti2": "Ei kuvaajaa tallennettavana",
    "virheviesti3": "Tasoitus ei toimi",
    "piirtoalue": None,
    "kuvaaja": None,
    "xpisteet": [],
    "ypisteet": [],
    "linydata": np.array([]),
    "kehys1": None,
    "kehys2": None,
    "ikkuna": None,
    "laatikko1": None,
    "laatikko2": None,
    "xdata": np.array([]),
    "ydata": np.array([]),
}


def poista_lineaarinen_tausta():
    """
    Poistaa lineaarisen taustan kuvaajasta.
    lasket suoran parametrit, niiden avulla suoran y-arvot x-akselin pisteissä, ja vähennät ne y-arvot y-datan vastaavista pisteistä
    """
    try:
        i = 0
        #datapisteiden valinta
        xpoint0 = elementit["xpisteet"][-2]; xpoint1 = elementit["xpisteet"][-1]
        ypoint0 = elementit["ypisteet"][-2]; ypoint1 = elementit["ypisteet"][-1]

        kulmakerroin = float((ypoint1 - ypoint0) / (xpoint0 - xpoint1))
        vakiotermi = float((xpoint0 * ypoint1 - xpoint0 * ypoint1) / (xpoint1 - xpoint0))

        #linydatan putsaus ennen uusia laskuja
        for j in range(len(elementit["linydata"])):
            elementit["linydata"] = np.delete(elementit["linydata"], [0])
        
        #linydatan laskenta
        for k in range(len(elementit["ydata"])):
            try:
                y = kulmakerroin * elementit["xdata"][i] + vakiotermi
                yvanha = elementit["ydata"][i]
                newy = yvanha - y
                elementit["linydata"] = np.append(elementit["linydata"], newy)
                i += 1
            except IndexError:
                continue
        #kuvaajan piirto
        elementit["ax"].cla()
        elementit["ax"].set_xlabel("Binding energy(eV)")
        elementit["ax"].set_ylabel("Intensity (arbitary units)")
        elementit["ax"].plot(elementit["xdata"], elementit["linydata"])
        elementit["piirtoalue"].draw()
    except ValueError:
        ik.kirjoita_tekstilaatikkoon(elementit["laatikko1"],
        elementit["virheviesti3"], tyhjaa=False)
        return


def laske_ydata(y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19):
    i = 0
    try:
        for x in range(len(y1)):
            y = y0[i]+y1[i]+y2[i]+y3[i]+y4[i]+y5[i]+y6[i]+y7[i]+y8[i]+y9[i]+y10[i]+y11[i]+y12[i]+y13[i]+y14[i]+y15[i]+y16[i]+y17[i]+y18[i]+y19[i]
            elementit["ydata"] = np.append(elementit["ydata"], y)
            i += 1
    except IndexError:
        return


def lue_data(path):
    """
    Lukee kaikki tiedostot annetusta kansiosta. Ohittaa tiedostot, jotka eivät
    ole päätteeltään .txt ja tallentaa ne dictissä oleviin listoihin xdata ja ydata.
    """
    luku = 0
    x0 = []
    y0 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    y7 = []
    y8 = []
    y9 = []
    y10 = []
    y11 = []
    y12 = []
    y13 = []
    y14 = []
    y15 = []
    y16 = []
    y17 = []
    y18 = []
    y19 = []
    files = []
    try:
        for filename in os.listdir(path): #lukee kansion
            if filename.endswith(".txt"):    #tarkastaa tiedostopäätteet
                files.append(filename)
                with open(os.path.join(path, filename)) as kohde:  #avaa tiedoston
                    for z in kohde:
                        lines = kohde.read()     #lukee tiedoston
                        line = lines.split("\n")    #splittaa rivinvaihdosta listaan
                        file_len = len(line)
                        for i in range(file_len):
                            rivi = line[i]
                            try: #vaihtaa listan alkioden muodon stringistä float ja tallentaa ne listaan
                                rivi.rstrip()
                                lista = rivi.split(" ")
                                ekafloat = float(lista[0])
                                tokafloat = float(lista[1])
                                if luku == 0:
                                    y0.append(tokafloat)
                                elif luku == 1:
                                    y1.append(tokafloat)
                                elif luku == 2:
                                    y2.append(tokafloat)
                                elif luku == 3:
                                    y3.append(tokafloat)
                                elif luku == 4:
                                    y4.append(tokafloat)
                                elif luku == 5:
                                    y5.append(tokafloat)
                                elif luku == 6:
                                    y6.append(tokafloat)
                                elif luku == 7:
                                    y7.append(tokafloat)
                                elif luku == 8:
                                    y8.append(tokafloat)
                                elif luku == 9:
                                    y9.append(tokafloat)
                                elif luku == 10:
                                    y10.append(tokafloat)
                                elif luku == 11:
                                    y11.append(tokafloat)
                                elif luku == 12:
                                    y12.append(tokafloat)
                                elif luku == 13:
                                    y13.append(tokafloat)
                                elif luku == 14:
                                    y14.append(tokafloat)
                                elif luku == 15:
                                    y15.append(tokafloat)
                                elif luku == 16:
                                    y16.append(tokafloat)
                                elif luku == 17:
                                    y17.append(tokafloat)
                                elif luku == 18:
                                    y18.append(tokafloat)
                                elif luku == 19:
                                    x0.append(ekafloat)
                                    y19.append(tokafloat)
                            except ValueError:
                                pass
                        luku += 1
                    elementit["xdata"] = np.append(elementit["xdata"], x0)
                    laske_ydata(y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19)
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
        if elementit["xdata"].size > 0 and elementit["ydata"].size > 0:
            elementit["ax"].cla()
            elementit["ax"].plot(elementit["xdata"], elementit["ydata"])
            elementit["ax"].set_xlabel("Binding energy(eV)")
            elementit["ax"].set_ylabel("Intensity (arbitary units)")
            elementit["piirtoalue"].draw()
        else:
            ik.kirjoita_tekstilaatikkoon(elementit["laatikko1"],
            elementit["virheviesti"], tyhjaa=False)
    except ValueError:
        ik.kirjoita_tekstilaatikkoon(elementit["laatikko1"],
        elementit["virheviesti"], tyhjaa=False)

def tallennus():
    if elementit["xdata"].size > 0 and elementit["ydata"].size > 0:
        polku = ik.avaa_tallennusikkuna("Tallenna kuvaaja")
        elementit["kuvaaja"].savefig(polku)
    else:
        ik.kirjoita_tekstilaatikkoon(elementit["laatikko1"],
        elementit["virheviesti2"], tyhjaa=False)

def laske_intensiteetti():
    try:
        xpoints = []
        xdata1 = []
        xslice = 0; yslice = []
        x0 = elementit["xpisteet"][-2]; x1 = elementit["xpisteet"][-1]
        xpoints.append(x0); xpoints.append(x1)
        i = 0
        for k in range(len(elementit["xdata"])):
            numba = elementit["xdata"][i]
            xdata1.append(numba)
            i += 1
        xclosest0 = min(xdata1, key=lambda x: abs(x-x0))
        x0index = xdata1.index(xclosest0)
        xclosest1 = min(xdata1, key=lambda x: abs(x-x1))
        x1index = xdata1.index(xclosest1)
        xslice = elementit["xdata"][x0index:x1index]
        yslice = elementit["linydata"][x0index:x1index]
        try:
            integraali = abs(np.trapz(yslice, xslice))
            ik.kirjoita_tekstilaatikkoon(elementit["laatikko1"],
            "Piikin intensiteetti on: {:.4f}".format(integraali))
        except ValueError:
            ik.kirjoita_tekstilaatikkoon(elementit["laatikko1"], "Tasoita kuvaaja ensin (poista lineaarinen tausta)")
        xpoints.clear()
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