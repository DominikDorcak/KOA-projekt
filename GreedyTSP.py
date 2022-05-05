
import random
import numpy as np


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
        minvzd = np.inf
        minindex = None
        cindex = None
        for uin,u in enumerate(C):
            for v, vzd in enumerate(mapa[u]):
                if v not in C:
                    if vzd < minvzd:
                        minvzd = vzd
                        minindex = v
                        cindex = uin

        if debug: print("pridavam vrchol:", minindex)
        k += 1
        C.insert(cindex, minindex)
        if debug: print("priebezna kruznica",C)

    if debug: print("Ukoncujem Algoritums")
    return C