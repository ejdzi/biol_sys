import ast


#### start the script by typing in python: from TreeMaker import *; form_pre_generated_list()

def maketree(el, nl=None):
    if nl is None:
        nl = []
    edgelist = el[::-1]  # edge list is supplied in order of removal from graph, work has to be done in reverse order
    treelist = []  # list will contain all leaves which will be joined into subtrees until one tree is formed
    nodelist = set(nl)  # list of all nodes of the graph, which will be the tree's leaves

    if len(nl) == 0:
        manualnl = set()
        for edge in edgelist:  # Manual node list making if not provided
            nod1 = edge[0]
            nod2 = edge[1]
            manualnl.add(nod1)
            manualnl.add(nod2)
        nodelist = manualnl
    for n in nodelist:
        treelist.append(({n}, n))  # creation of treelist.
    # treelist always holds tuples of (Set of all leaves of the subtree, subtree structure)'
    for edge in edgelist:
        nod1 = edge[0]
        nod2 = edge[1]  # nodes extracted from edge
        joim1 = 0
        joim2 = 0  # subtrees to be joined in this step
        for t in treelist:
            if nod1 in t[0]:
                joim1 = t
            if nod2 in t[0]:
                joim2 = t  # subtrees to be joined are found by checking if their leaf sets contain the two nodes of the given edge
        if not joim1 == joim2:  # if the two nodes are in the same subtree, no joining needs to be done
            treelist.remove(joim1)
            treelist.remove(joim2)  # the two subtrees are removed from the treelist
            newset = joim1[0].union(joim2[0])  # leaf set of the new subtree
            treelist.append((newset, (joim1[1], joim2[1])))  # and replaced with a subtree consisting of them joined
        if len(treelist) == 1:  # we don't need to keep going if we only have one subtree
            return treelist[0][1]  # returns subtree structure only
    return treelist[0][1]  # returns subtree structure only


def form_pre_generated_list():
    global cos2
    with open('lista.txt', 'r') as file:
        cos = file.read()
        cos2 = ast.literal_eval(cos)  # this is the script to take out the list from the file
    maketree(cos2)


