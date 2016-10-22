from grafy import *
from edges import *
from nodes import *

G = load_graph('l.gexf')
G = make_undireced_graph(G)
add_betweenness_edge(G)
add_betweenness_node(G)

print "Betweenness for first EDGE is", get_edge_parameter(G, G.edges()[0], 'bet')
print "\nBetweenness for first NODE is", get_node_parameter(G, G.nodes()[0], 'bet')

print "\nWierzcholki malejoco posortowane wzgledem betweenness"
for node in get_nodes_sorted_by(G, 'bet', True):
    print node

print '\n\nKrawedzie posortowane rosnaco wartosci betweenness'
for edge in get_edges_sorted_by(G, 'bet', False):
    print edge
