# wymagany jest tylko networkx (a co za tym idzie chyba numpy)
""" w tym pliku znajduja sie ogolne rzeczy dotyczace grafow"""
import networkx as nx


def load_graph(gefx_file):
    """ wczytwanie grafu z pliku gefx"""
    return nx.read_gexf(gefx_file, relabel=True)


def make_undireced_graph(graf):
    """ zamiania graf na graf nieskierowany (zazwycaj to robilismy) """
    return graf.to_undirected()


def get_edge_parameter(graf, edge, parameter):
    """ mozna pobrac jakis parametr dla wierzcholka"""
    return graf[edge[0]][edge[1]][parameter]


def get_node_parameter(graf, node, parameter):
    """ mozna pobrac jakis parametr dla krawedzi """
    return graf.node[node][parameter]


def print_graph(graf):
    """ jak ktos nie chce rysowac to nie musi, stad import jest tutaj """
    import matplotlib.pyplot as plt
    nx.draw(graf, with_labels=True)
    plt.show()


def get_nodes_sorted_by(graf, parameter, malejaco=True):
    result = []
    for node in graf.nodes():
        result.append((node, graf.node[node][parameter]))
    result.sort(key=lambda tupla: tupla[1], reverse=malejaco)
    return result


def get_edges_sorted_by(graf, parametr, malejaco=True):
    result = []
    for edge in graf.edges():
        result.append((edge, graf[edge[0]][edge[1]][parametr]))
    result.sort(key=lambda tupla: tupla[1], reverse=malejaco)
    return result
