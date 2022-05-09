import numpy as np


class MatchingGenerator:

    def __init__(self, V, mapa):
        self.V = V
        self.arr = [None for v in V]
        self.inArr = [False for v in V]
        self.mapa = mapa
        self.minval = np.inf
        self.matching = []

    def process(self):
        matching = []
        for i in range(len(self.arr) // 2):
            matching.append([self.V[self.arr[2 * i]], self.V[self.arr[2 * i + 1]]])
        matchingvalue = self.matchingValue(matching)
        if matchingvalue < self.minval:
            self.minval = matchingvalue
            self.matching = matching

    def matchingValue(self, matching):
        val = 0
        for m in matching:
            val += self.mapa[m[0], m[1]]
        return val

    def generate(self, index):
        if index == len(self.arr):
            self.process()
            return
        for i in range(len(self.V)):
            if not self.inArr[i]:
                self.inArr[i] = True
                self.arr[index] = i
                self.generate(index + 1)
                self.inArr[i] = False

    def minMatching(self):
        self.generate(0)
        return self.matching
