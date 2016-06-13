# wymagany jest tylko networkx (a co za tym idzie chyba numpy)
"""w tym pliku znajduja sie wszystkie rzeczy ktroe mozna dodac do wierzcholka"""
import networkx as nx


def add_betweenness_edge(graf):
    print "Adding betweenness to edges"
    b_dict = nx.edge_betweenness_centrality(graf)
    nx.set_edge_attributes(graf, 'bet', b_dict)


def add_commonality_edge(graf):
    print "Adding commonality to edges"
    commonality = {}
    for edge in graf.edges_iter():
        node1 = edge[0]
        node2 = edge[1]
        neighbours1 = nx.all_neighbors(graf, node1)
        neighbours2 = nx.all_neighbors(graf, node2)
        set1 = set(neighbours1)
        set2 = set(neighbours2)
        k = len(set1.intersection(set2))
        n = len(set1)
        m = len(set2)
        com = (k + 1) / (n * m) ** 0.5
        commonality[edge] = com
    nx.set_edge_attributes(graf, 'com', commonality)


# od tego miejsca bardziej "egzotyczne" miary

def add_load_edge(graf):
    print "Adding load to edges"
    l_dict = nx.edge_load(graf)
    nx.set_edge_attributes(graf, 'loa', l_dict)


def add_current_flow_betweenness_edge(graf):
    print "Adding current flow betweenness to edges"
    cfb_dict = nx.edge_current_flow_betweenness_centrality(graf)
    nx.set_edge_attributes(graf, 'cfb', cfb_dict)
