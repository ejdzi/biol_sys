import networkx as nx
from wejscie import add_betweenness, add_communality


def lazy_remove_edges(graf):
    deleted_edges = []
    while nx.number_of_edges(graf) != 0:
        max_edge = None
        max_bc = 0
        for edge in graf.edges():
            bc = graf[edge[0]][edge[1]]['bet'] / graf[edge[0]][edge[1]]['com']
            if bc > max_bc:
                max_edge = edge
        deleted_edges.append(max_edge)
        if max_edge[0] and max_edge[1]:
            graf.remove_edge(max_edge[0], max_edge[1])
        #no betweenness recalculation
    return deleted_edges

def bad_remove_edges(graf):
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
        add_communality(graf) #added commonality recalculation
    return deleted_edges

def weight_remove_edges(graf):
    deleted_edges = []
    while nx.number_of_edges(graf) != 0:
        max_edge = None
        max_bc = 0
        for edge in graf.edges():
            bc = graf[edge[0]][edge[1]]['weight'] * graf[edge[0]][edge[1]]['bet'] / graf[edge[0]][edge[1]]['com'] #multiplies in a 'weight' edge parameter
            if bc > max_bc:
                max_edge = edge
        deleted_edges.append(max_edge)
        graf.remove_edge(max_edge[0], max_edge[1])
        add_betweenness(graf)
    return deleted_edges

