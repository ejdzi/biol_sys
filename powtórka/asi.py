# coding=utf-8
from copy import copy

__author__ = 'joanna'
plik = open("yeastHighQuality.sif")

# znajdowanie hubow
spis = {}
spis1 = {}
# dla kazdej liniki
for p in plik:
    # tnie linie po przerwach
    line = p.strip().split()
    # przechodzi przez pociete linie
    # sprawdzenie czy jest juz na liscie
    if len(line) == 0:
        continue
    if line[0] not in spis.keys():
        spis[line[0]] = [line[-1]]

    elif line[0] in spis.keys() and line[-1] not in spis[line[0]]:
        spis[line[0]].append(line[-1])
    if line[-1] not in spis.keys():
        spis[line[-1]] = [line[0]]
    elif line[-1] in spis.keys() and line[0] not in spis[line[-1]]:
        spis[line[-1]].append(line[0])
plik.close()

najwieksz = 0
id_bial = ""
hubuw = len(spis.keys()) / 10
while len(spis1.keys()) < hubuw:
    for s in spis.items():
        if najwieksz < len(s[1]):
            najwieksz = len(s[1])
            id_bial = s[0]
    spis1[id_bial] = copy(spis[id_bial])

    spis.pop(id_bial)
    najwieksz = 0
print spis1.keys(), len(spis1.keys())
