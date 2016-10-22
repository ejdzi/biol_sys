# wymagany jest tylko networkx (a co za tym idzie chyba numpy)
import networkx as nx


def add_degree_node(graf):
    print "Adding degree to nodes"
    d_dict = nx.degree_centrality(graf)
    nx.set_node_attributes(graf, 'deg', d_dict)


def add_in_degree_node(graf):
    print "Adding IN degree to nodes"
    d_dict = nx.in_degree_centrality(graf)
    nx.set_node_attributes(graf, 'deg_in', d_dict)


def add_out_degree_node(graf):
    print "Adding OUT degree to nodes"
    d_dict = nx.out_degree_centrality(graf)
    nx.set_node_attributes(graf, 'deg_out', d_dict)


def add_closeness_node(graf):
    print "Adding closensess to nodes"
    c_dict = nx.closeness_centrality(graf)
    nx.set_node_attributes(graf, 'clo', c_dict)


def add_betweenness_node(graf):
    print "Adding betweenness to nodes"
    b_dict = nx.betweenness_centrality(graf)
    nx.set_node_attributes(graf, 'bet', b_dict)


def add_eigenvector_node(graf):
    print "Adding eigenvector to nodes"
    e_dict = nx.eigenvector_centrality(graf)
    nx.set_node_attributes(graf, 'eig', e_dict)


def add_katz_node(graf):
    print "Adding katz to nodes"
    k_dict = nx.katz_centrality(graf)
    nx.set_node_attributes(graf, 'kat', k_dict)


# od tego mejsca jakies bardziej "egzotyczne" miary

def add_current_flow_closeness_node(graf):
    print "Adding current flow CLOSENESS to nodes"
    cfc_dict = nx.current_flow_closeness_centrality(graf)
    nx.set_node_attributes(graf, 'cfc', cfc_dict)


def add_current_flow_betweenness_node(graf):
    print "Adding current flow BETWEENNESS to nodes"
    cfb_dict = nx.current_flow_betweenness_centrality(graf)
    nx.set_node_attributes(graf, 'cfb', cfb_dict)


def add_communicability_betweenness_node(graf):
    print "Adding communicability betweenness to nodes"
    cmb_dict = nx.communicability_betweenness_centrality(graf)
    nx.set_node_attributes(graf, 'cmb', cmb_dict)


def add_load_node(graf):
    print "Adding load to nodes"
    l_dict = nx.load_centrality(graf)
    nx.set_node_attributes(graf, 'loa', l_dict)
