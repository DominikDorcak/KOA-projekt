
from utils import eulerianPath, Jarnik


def DoubleSpanningTreeTSP(mapa,debug=False):
    if debug: print("ZACINAM TSP ALGORITMUS ZDVOJENIM KOSTRY")
    # Krok 1 - vypocitame minimalnu kostru
    T = Jarnik(mapa)
    if debug: print("Jarnikovym algoritmom vygenerovana minimalna kostra:", T)
    # Krok 2 - zdvojime hrany
    H = T.copy()
    for e in T:
        H.append([e[1], e[0]])
    # Krok 3 - najdenie eulerovskeho tahu
    ep = eulerianPath(H)
    if debug: print("Zasobnikovym algoritmom najdeny eulerovsky tah", ep)
    # Krok 4 - pridavanie vrcholov z tahu do kruznice
    kruznica = []
    for v in ep:
        if v not in kruznica:
            kruznica.append(v)
    return kruznica

