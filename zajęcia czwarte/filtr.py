proteasom = ['YOR362C', 'YPR103W', 'YJL001W', 'YOL038W', 'YER094C', 'YGL011C', 'YML092C']
mapa = {}
mapa['Pre10'] = proteasom[0]
mapa['Pre2'] = proteasom[1]
mapa['Pre3'] = proteasom[2]
mapa['Pre6'] =  proteasom[3]
mapa['Pup3'] = proteasom[4]
mapa['Scl1'] = proteasom[5]
mapa['Pre8'] = proteasom[6]
interakcje = {}
interakcje['Pre10'] = ['Pre3', 'Pre6', 'Scl1']
interakcje['Pre2'] = ['Pre10', 'Pre3', 'Pre6','Scl1']
interakcje['Pre3'] = ['Pre10', 'Scl1']
interakcje['Pre6'] = ['Pre10', 'Pre3', 'Scl1']
interakcje['Pup3'] = ['Pre10', 'Pre3', 'Pre6' , 'Scl1']
interakcje['Pre8'] = ['Scl1']
plik = open('yeastHighQuality.sif')
linie = plik.readlines()
for (k, vv) in interakcje.items():
	for v in vv:
		jest = False
		for l in linie:
			if (mapa[k] in l) and (mapa[v] in l):
				jest = True
				break
		if not jest:
			print k, v
wszystkie = {}
for p in proteasom:
	wszystkie[p] = []
	for pp in proteasom:
		for l in linie:
			if p!=pp and p in l and pp in l:
				wszystkie[p].append(pp)
for w in wszystkie.values():
	print len(w)