import numpy as np

from Stack import Stack


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


def Jarnik(mapa):
    V = []
    E = []
    i = 1
    min1 = np.inf
    e1 = None
    for x in range(len(mapa)):
        for y in range(len(mapa)):
            if x != y:
                if (mapa[x][y]) < min1:
                    min1 = mapa[x][y]
                    e1 = [x, y]
    V.append(e1[0])
    V.append(e1[1])
    E.append(e1)
    i += 1
    while True:
        Fcount = 0
        minimum = np.inf
        ei = None
        yi = None
        for x in range(len(mapa)):
            for y in range(len(mapa)):
                if x != y:
                    if x in V and y not in V:
                        Fcount += 1
                        if (mapa[x][y]) < minimum:
                            minimum = mapa[x][y]
                            ei = [x, y]
                            yi = y
        if Fcount == 0: return E
        V.append(yi)
        E.append(ei)
        i = i + 1


def eulerianPath(H):
    C = [0 for e in H]
    print(H)
    EP = []
    stack = Stack()
    stack.push(0)
    while not stack.isEmpty():
        x = stack.peek()
        add = False
        for index, e in enumerate(H):
            if e[0] == x and  C[index] == 0:
                    stack.push(e[1])
                    C[index] = 1
                    add = True
                    break
            if e[1] == x and C[index] == 0:
                    stack.push(e[0])
                    C[index] = 1
                    add = True
                    break
        if not add:
            top = stack.pop()
            EP.append(top)
    return EP
