# Zadanie 4.(D. Dorčák)
# Kuriérska spoločnosť potrebuje nájsť prekuriéra optimálnu trasu, vrámci ktorej má navštíviť každé miesto doručenia, vrátiť sa tam, odkiaľ vyrážal, a prejsť celú
# trasu čo najrýchlejšie. Vstup je zadaný (vo forme textového súboru) tabuľkou, vktorej v i-tom riadku aj-tom stĺpci je daná dĺžka cesty z miesta i do miesta j.
# Program má nájsť postupnosť jednotlivých miest doručenia tak, aby kuriér prešiel všetky miesta doručenia a aby prešiel čo najmenšiu vzdialenosť.
import datetime
import numpy as np

from GreedyTSP import greedyTSP
from DoubleSpanningTreeTSP import DoubleSpanningTreeTSP

def load_text(filename="vstup.txt", separator=" "):
    with open(filename, "r") as vstup:
        mapa = []
        for riadok in vstup.readlines():
            vzdialenosti = riadok.split(separator)
            mapa.append([int(v) for v in vzdialenosti])
        vstup.close()
        return np.array(mapa)

def dlzka_kruznice(kruznica,mapa):
    sucet = 0
    for i in range(1,len(kruznica)):
        sucet += mapa[kruznica[i-1]][kruznica[i]]
    sucet += mapa[kruznica[-1]][kruznica[0]]
    return sucet

def TSP(debug=False):
    mapa = load_text(filename="vstup.txt")
    print(mapa)

    start = datetime.datetime.now()
    print("GREEDY:")
    kruznica = greedyTSP(mapa, debug,start=0)
    time = datetime.datetime.now() - start
    print("najdena kruznica:", kruznica, "dlzka: kruznice:", dlzka_kruznice(kruznica,mapa),  "celkovy cas vypoctu:", time.total_seconds() * 1000)

    start = datetime.datetime.now()
    print("ZDVOJENIE KOSTRY:")
    kruznica = DoubleSpanningTreeTSP(mapa, debug)
    time = datetime.datetime.now() - start
    print("najdena kruznica:", kruznica, "dlzka: kruznice:", dlzka_kruznice(kruznica, mapa), "celkovy cas vypoctu:",
          time.total_seconds() * 1000)


if __name__ == '__main__':
    TSP(debug=True)
