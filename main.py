# Zadanie 4.(D. Dorčák)
# Kuriérska spoločnosť potrebuje nájsť prekuriéra optimálnu trasu, vrámci ktorej má navštíviť každé miesto doručenia, vrátiť sa tam, odkiaľ vyrážal, a prejsť celú
# trasu čo najrýchlejšie. Vstup je zadaný (vo forme textového súboru) tabuľkou, vktorej v i-tom riadku aj-tom stĺpci je daná dĺžka cesty z miesta i do miesta j.
# Program má nájsť postupnosť jednotlivých miest doručenia tak, aby kuriér prešiel všetky miesta doručenia a aby prešiel čo najmenšiu vzdialenosť.
import datetime
import random
import numpy as np
from enum import Enum


class GrowthDirection(Enum):
    DIRECTION_NONE = 0
    DIRECTION_FROM_START = 1
    DIRECTION_FROM_END = 2


def load_text(filename="vstup.txt", separator=" "):
    with open(filename, "r") as vstup:
        mapa = []
        for riadok in vstup.readlines():
            vzdialenosti = riadok.split(separator)
            mapa.append([int(v) for v in vzdialenosti])
        vstup.close()
        return np.array(mapa)


# GREEDY algoritmus na hladanie min. Hamiltonovskej kruznice
def greedyTSP(mapa, debug=False, start=np.NaN):
    # prvy krok - nahodny zaciatocny vrchol
    if debug: print("ZACINAM GREEDY TSP ALGORITMUS")
    k = 1
    if np.isnan(start): start = random.randint(0, len(mapa) - 1)
    if debug: print('startujuci vrchol:', start)
    C = [start]
    dlzka = 0
    # druhy krok - hladanie minimalnej hrany z vrcholov v kruznici do vrcholov mimo kruznice
    while k < len(mapa):
        start, end = C[0], C[-1]
        if debug: print("KROK", k);print("novy zaciatok:", start, "novy koniec:", end)
        minvzd = np.inf
        minindex = None
        direction = GrowthDirection.DIRECTION_NONE
        for v, vzd in enumerate(mapa[start]):
            if v not in C:
                if vzd < minvzd:
                    minvzd = vzd
                    minindex = v
                    direction = GrowthDirection.DIRECTION_FROM_START
        for v, vzd in enumerate(mapa[end]):
            if v not in C:
                if vzd < minvzd:
                    minvzd = vzd
                    minindex = v
                    direction = GrowthDirection.DIRECTION_FROM_END
        # treti krok
        if debug: print("pridavam vrchol:", minindex,
                        ("na zaciatok" if direction == GrowthDirection.DIRECTION_FROM_START else "na koniec"),
                        "min vzdialenost:", minvzd)
        k += 1
        if direction == GrowthDirection.DIRECTION_FROM_START:
            C.insert(0, minindex)
        elif direction == GrowthDirection.DIRECTION_FROM_END:
            C.append(minindex)
        dlzka += minvzd

    start, end = C[0], C[-1]
    if debug: print("Ukoncujem Algoritums")
    if debug: print("pridavam najkratsiu cestu medzi zaciatkom a koncom cesty(", start, "a", end, ")")
    if mapa[end][start] < mapa[start][end]:
        C.append(start)
        dlzka += mapa[end][start]
        if debug: print("dlzka cesty:",mapa[end][start])
    else:
        C.insert(0, end)
        dlzka += mapa[start][end]
        if debug: print("dlzka cesty:",mapa[start][end])
    return C, dlzka


def TSP(debug=False):
    mapa = load_text(filename="vstup2.txt")
    print(mapa)
    start = datetime.datetime.now()
    print("GREEDY:")
    kruznica, dlzka = greedyTSP(mapa, debug)
    time = datetime.datetime.now() - start
    print("najdena kruznica:", kruznica, "dlzka: kruznice:", dlzka, "celkovy cas vypoctu:", time.total_seconds() * 1000)


if __name__ == '__main__':
    TSP(debug=True)
