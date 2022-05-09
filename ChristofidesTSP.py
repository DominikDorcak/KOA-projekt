import numpy as np

from MatchingGenerator import MatchingGenerator
from utils import Jarnik, oddDegreeVertices, eulerianPath


def ChristofidesTSP(mapa, debug=False):
    if debug: print("ZACINAM  Christofides TSP ALGORITMUS")
    # Krok 1 - vypocitame minimalnu kostru T, O je mnozina vrcholov s neparnym stupnom v T
    T = Jarnik(mapa)
    if debug: print("Jarnikovym algoritmom vygenerovana minimalna kostra:", T)
    O = oddDegreeVertices(T)
    if debug: print("Neparne vrcholy:", O)
    # Krok 2 - najdenie optimalneho sparenia M
    generator = MatchingGenerator(O,mapa)
    M = generator.minMatching()
    if debug: print("Minimalne sparenie pomocou backtracku cez O :", M)
    # Krok 3 - zostrojime eulerovsky graf zlucenim M a T
    H = T.copy()
    H.extend(M)
    if debug: print("Zlucenie sparenia a kostry:", H)
    # Krok 4 - eulerovsky tah a kruznica ako pri DoubleSpanningTreeTSP
    ep = eulerianPath(H)
    if debug: print("Zasobnikovym algoritmom najdeny eulerovsky tah", ep)
    kruznica = []
    for v in ep:
        if v not in kruznica:
            kruznica.append(v)
    return kruznica
