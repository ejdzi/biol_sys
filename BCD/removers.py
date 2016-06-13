# coding=utf-8
import networkx as nx
from wejscie import add_betweenness, add_commonality


###szybszy sposób
def lazy_remove_edges(graf):
    deleted_edges = []
    while nx.number_of_edges(graf) != 0:
        max_edge = None
        max_bc = 0
        for edge in graf.edges():
            bc = graf[edge[0]][edge[1]]['bet'] / graf[edge[0]][edge[1]]['com']
            if bc >= max_bc:
                max_edge = edge
        deleted_edges.append(max_edge)
        graf.remove_edge(max_edge[0], max_edge[1])
        # no betweenness recalculation
    return deleted_edges


###gorszy sposób
def bad_remove_edges(graf):
    deleted_edges = []
    while nx.number_of_edges(graf) != 0:
        max_edge = None
        max_bc = 0
        for edge in graf.edges():
            bc = graf[edge[0]][edge[1]]['bet'] / graf[edge[0]][edge[1]]['com']
            if bc >= max_bc:
                max_edge = edge
        deleted_edges.append(max_edge)
        if max_edge:
            graf.remove_edge(max_edge[0], max_edge[1])
        add_betweenness(graf)
        add_commonality(graf)  # added commonality recalculation
    return deleted_edges


###wagi
def weight_remove_edges(graf):
    deleted_edges = []
    while nx.number_of_edges(graf) != 0:
        max_edge = None
        max_bc = 0
        for edge in graf.edges():
            try:
                weight = graf[edge[0]][edge[1]]['weight']
            except:
                weight = 1
            bc = weight * graf[edge[0]][edge[1]]['bet'] / graf[edge[0]][edge[1]][
                'com']  # multiplies in a 'weight' edge parameter
            if bc >= max_bc:
                max_edge = edge
        deleted_edges.append(max_edge)
        if max_edge:
            graf.remove_edge(max_edge[0], max_edge[1])
        add_betweenness(graf)
    return deleted_edges
