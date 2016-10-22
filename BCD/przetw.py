from math import sqrt
import sets

__author__ = 'joanna'
import networkx as nx


def przetworz(graf):
    comminity = {}
    for edge in graf.edges_iter():
        node1 = edge[0]
        node2 = edge[1]
        neighbaours1 = nx.all_neighbors(graf, node1)
        neighbaours2 = nx.all_neighbors(graf, node2)
        set1 = sets.Set(neighbaours1)
        set2 = sets.Set(neighbaours2)
        k = len(set1.intersection(set2))
        n = len(set1)
        m = len(set2)
        com = (k + 1) / (sqrt(n * m))
        comminity[edge] = com

        print node1, node2, neighbaours1, neighbaours2, set1, set2, k, com

    nx.set_edge_attributes(graf, "com", comminity)
    print comminity


G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
H = nx.path_graph(10)
G.add_nodes_from(H)
G.add_edge(1, 2)
G.add_edge(3, 2)
G.add_edge(1, 3)
print nx.edge_betweenness_centrality(G)
nx.all_neighbors(G, 1)
przetworz(G)
