# coding=utf-8
from math import sqrt

import networkx as nx

from TreeMaker import maketree

from ete2 import Tree, TreeStyle, NodeStyle
from random import choice
from copy import deepcopy

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
        set1 = set(neighbaours1)
        set2 = set(neighbaours2)
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

def color():
    k = "#"
    for i in range(3): k += choice(["AA","BB","CC","DD","77","88","99"])
    return k

def find_modules_and_draw_tree(drzewo, graph):
    t = Tree(str(drzewo)+";")
    t.img_style["bgcolor"] = "lavender"
    ts = TreeStyle()

    special = set() #defaultdict(list)
    for l in t.iter_leaves():
        tmp = l
        special.add(tmp)
        up = True
        while up:
            up = False
            if tmp.is_root():
                break
            else:
                for children in tmp.up.children:
                    if children.is_leaf():
                        tmp = tmp.up
                        special.add(tmp)
                        up = True
                        break
    modules = set()
    for node in t.traverse('preorder'):
        if node in special:
            good = True
            for n in node.traverse('preorder'):
                if n not in special:
                    good = False
                    break
            if good:
                if not node.is_leaf(): modules.add(node)
                for n in node.traverse('preorder'):
                    special.remove(n)

    # below: merging modules by pre-defined cutoff
    def check_modules(i,j,graph,cutoff):
        for ii in i.iter_leaves():
            for jj in j.iter_leaves():
                if ii.name[1:-1] in graph[jj.name[1:-1]] and graph[jj.name[1:-1]][ii.name[1:-1]]["com"] > cutoff:
                    return True
        return False

    while True:
        breakkk = False
        for i in modules:
            if breakkk: break
            for j in modules:
                if i!=j and (not i.is_root()) and i.up == j.up and check_modules(i,j,graph, 0.1): # CUTOFF HERE
                    breakkk = True
                    break
        if breakkk:
            modules.add(i.up)
            modules.remove(i)
            modules.remove(j)
        else: break # heh...

    ts.show_leaf_name = True
    for i in modules:
        style_ca = NodeStyle()
        style_ca["bgcolor"] = color()
        i.set_style(style_ca)
    t.show(tree_style=ts)


def run(filename):
    graf = load_graph(filename)
    graf_copy = deepcopy(graf)
    usuniete_krawedzie = remove_edges(graf)
    drzewo = maketree(usuniete_krawedzie)
    find_modules_and_draw_tree(drzewo, graf_copy)


run('l.gexf')