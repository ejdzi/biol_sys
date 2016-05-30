# coding=utf-8
from collections import defaultdict

d = defaultdict(list)
with open('yeastHighQuality.sif') as f:
    for line in f:
        l = line.strip().split()
        if l[1] == 'pp' or l[1] == 'pd':
            d[l[0]].append(l[2])
            d[l[2]].append(l[0])
huby = d.items()
huby.sort(key=lambda i: len(i[1]))
huby = huby[-int(len(d) * 0.1):]
print 'Hubów mamy:', len(huby)
d = defaultdict(set)
for h in xrange(len(huby)):
    for hh in xrange(len(huby)):
        if (huby[h][0] in huby[hh][1]) or (huby[hh][0] in huby[h][1]):
            d[huby[h][0]].add(huby[hh][0])
            d[huby[hh][0]].add(huby[h][0])
print 'Ilość hubów oddziałujących ze sobą:', len(d)
print 'Procent oddziałujących wzajemnie hubów:', float(len(d)) / len(huby) * 100
plik = open('wynik', 'w')
for (k, v) in d.items():
    plik.write(k + ': ' + str(v) + '\n')
plik.close()
