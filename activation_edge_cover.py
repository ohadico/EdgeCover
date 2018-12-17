import random
import sys
from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx

IS_MULTIGRAPH = True

random.seed(6)
G = nx.Graph() if not IS_MULTIGRAPH else nx.MultiGraph()

nodes = map(str, range(1, 6))
terminals = map(str, range(1, 6, 2))

for n in nodes:
    G.add_node(n)

for n1 in nodes:
    for n2 in nodes:
        if n1 != n2:
            G.add_edge(n1, n2, tu=random.randint(1, 10), tv=random.randint(1, 10))
            if IS_MULTIGRAPH:
                G.add_edge(n1, n2, tu=random.randint(1, 10), tv=random.randint(1, 10))

if IS_MULTIGRAPH:
    print("run neato -T png multigraph.dot > multigraph.png")
    nx.nx_pydot.write_dot(G, 'multigraph.dot')
    sys.exit()

pos = nx.spring_layout(G, seed=0)

nodes_drawing = nx.draw_networkx_nodes(G, pos, nodelist=terminals, node_color='r')
nodes_drawing.set_edgecolor('black')
nodes_drawing = nx.draw_networkx_nodes(G, pos, nodelist=set(nodes).difference(terminals), node_color='w')
nodes_drawing.set_edgecolor('black')

nx.draw_networkx_edges(G, pos)

edge_labels = nx.get_edge_attributes(G, 'tu')
nx.draw_networkx_edge_labels(G, pos,
                             edge_labels=edge_labels,
                             label_pos=0.1,
                             rotate=False)

edge_labels = nx.get_edge_attributes(G, 'tv')
nx.draw_networkx_edge_labels(G, pos,
                             edge_labels=edge_labels,
                             label_pos=0.9,
                             rotate=False)

plt.axis('off')

plt.savefig("activation_edge_cover.png")

plt.show()
