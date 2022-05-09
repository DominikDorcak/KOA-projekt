# Jarnikov algoritmus na hladanie minimalnej kostry
import numpy as np

from Stack import Stack


def load_text(filename="vstup.txt", separator=" "):
    with open(filename, "r") as vstup:
        mapa = []
        for riadok in vstup.readlines():
            vzdialenosti = riadok.split(separator)
            mapa.append([int(v) for v in vzdialenosti])
        vstup.close()
        return np.array(mapa)


def dlzka_kruznice(kruznica, mapa):
    sucet = 0
    for i in range(1, len(kruznica)):
        sucet += mapa[kruznica[i - 1]][kruznica[i]]
    sucet += mapa[kruznica[-1]][kruznica[0]]
    return sucet


def Jarnik(mapa):
    V = []
    E = []
    i = 1
    # pridanie prvej hrany umelo
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
    # ostatne hrany podla algoritmu
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


# najdenie eulerovskeho tahu pomocou zasobnika a oznacovania prejdenych hran
def eulerianPath(H):
    C = [0 for e in H]
    EP = []
    stack = Stack()
    stack.push(0)
    while not stack.isEmpty():
        x = stack.peek()
        add = False
        for index, e in enumerate(H):
            if e[0] == x and C[index] == 0:
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


def oddDegreeVertices(T):
    deg = {}
    for e in T:
        deg[e[0]] = deg[e[0]] + 1 if e[0] in deg else 1
        deg[e[1]] = deg[e[1]] + 1 if e[1] in deg else 1
    return [e for e in deg if deg[e] % 2 == 1]
