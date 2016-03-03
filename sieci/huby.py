# coding=utf-8
from collections import defaultdict
import matplotlib.pyplot as mtp
import statistics as stat

interact = defaultdict(set)

with open('data/Human_Interactome_May.sif') as plik:
    for line in plik.readlines():
        line_list = line.strip().split()
        if line_list[1] == 'pp':
            bialko1 = int(line_list[0])
            bialko2 = int(line_list[2])
            interact[bialko1].add(bialko2)
            interact[bialko2].add(bialko1)
wystapienia = []
liczba_polaczen = []
with open('output/output1.csv', 'w') as plik:
    for (k, v) in interact.items():
        ilosc_polaczen = len(v)
        liczba_polaczen.append((ilosc_polaczen, k))
        wystapienia.append(ilosc_polaczen)
        plik.write(str(k) + ',\t' + str(ilosc_polaczen) + '\n')

# mtp.hist(wystapienia, bins=500)
# mtp.show()
mean = stat.mean(wystapienia)
stdev = stat.pstdev(wystapienia)

with open('output/output2.csv', 'w') as plik:
    plik.write(str(mean) + ',\t' + str(stdev) + '\n')
liczba_polaczen.sort(reverse=True)
liczba_polaczen_met1 = liczba_polaczen[:int(len(liczba_polaczen) * 0.05)]
minimum1 = liczba_polaczen_met1[-1][0]
with open('output/output4.csv', 'w') as plik:
    for i in liczba_polaczen_met1:
        plik.write(str(i[1]) + ',\t' + str(i[0]) + '\n')
threshold = mean + 2 * stdev
minimum2 = None
with open('output/output5.csv', 'w') as plik:
    for i in liczba_polaczen:
        if i[0] >= threshold:
            plik.write(str(i[1]) + ',\t' + str(i[0]) + '\n')
            minimum2 = i[0]
        else:
            break
with open('output/output3.csv', 'w') as plik:
    plik.write(str(minimum1) + ',\t' + str(minimum2) + '\n')

############## DODATEK #############
# lol = interact
# for i in lol.keys():
#     yolo = True
#     ilosc = len(lol[i])
#     while yolo:
#         for sasiad in lol[i]:
#             lol[i] = lol[i].union(lol[sasiad])
#         if len(lol[i]) == ilosc:
#             yolo = False
