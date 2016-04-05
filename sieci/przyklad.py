# coding=utf-8
import networkx as nx
import matplotlib.pyplot as plt
import operator

G = nx.read_gexf('data/l.gexf', relabel=True)
G = G.to_undirected()
d = nx.edge_betweenness_centrality(G)
for (k, v) in d.items():
    print k, v
print 'Max', max(d.iteritems(), key=operator.itemgetter(1))
print 'Min', min(d.iteritems(), key=operator.itemgetter(1))
nx.draw(G, with_labels=True)
plt.show()
