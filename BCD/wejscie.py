# coding=utf-8
from math import sqrt

import networkx as nx
import sets


def add_betweenness(graf):
    b_dict = nx.edge_betweenness_centrality(graf)
    nx.set_edge_attributes(graf, 'bet', b_dict)


def add_communality(graf):
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
    nx.set_edge_attributes(graf, "com", comminity)


def load_graph(filename):
    graf = nx.read_gexf(filename, relabel=True)
    graf = graf.to_undirected()
    add_betweenness(graf)
    add_communality(graf)
    return graf


def remove_edges(graf):
    deleted_edges = []
    while nx.number_of_edges(graf) != 0:
        max_edge = None
        max_bc = 0
        for edge in graf.edges():
            bc = graf[edge[0]][edge[1]]['bet'] / graf[edge[0]][edge[1]]['com']
            if bc > max_bc:
                max_edge = edge
        deleted_edges.append(max_edge)
        graf.remove_edge(max_edge[0], max_edge[1])
        add_betweenness(graf)
    return deleted_edges


def buduj_drzewo(usuniete_krawedzie):
    pass


def rysuj_drzewo(drzewo):
    pass


def run(filename):
    graf = load_graph(filename)
    usuniete_krawedzie = remove_edges(graf)
    drzewo = buduj_drzewo(usuniete_krawedzie)
    rysuj_drzewo(drzewo)


run('l.gexf')
