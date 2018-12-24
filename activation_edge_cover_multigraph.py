import random
from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx

random.seed(6)
G = nx.MultiGraph()

nodes = map(str, range(1, 6))
terminals = map(str, range(1, 6, 2))

for n in nodes:
    G.add_node(n)

for i, n1 in enumerate(nodes[:-1]):
    for n2 in nodes[i+1:]:
        if n1 != n2:
            G.add_edge(n1, n2, tu=random.randint(1, 10), tv=random.randint(1, 10))
            G.add_edge(n1, n2, tu=random.randint(1, 10), tv=random.randint(1, 10))

pos = nx.spring_layout(G, seed=0)

nodes_drawing = nx.draw_networkx_nodes(G, pos, nodelist=terminals, node_color='r')
nodes_drawing.set_edgecolor('black')
nodes_drawing = nx.draw_networkx_nodes(G, pos, nodelist=set(nodes).difference(terminals), node_color='w')
nodes_drawing.set_edgecolor('black')

nx.draw_networkx_edges(G, pos)

edge_labels = defaultdict(str)
for edge in G.edges:
    if edge[:2] in edge_labels:
        edge_labels[edge[:2]] += '\n'
    edge_labels[edge[:2]] += "{tu}:{tv}".format(**G.edges[edge])
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.axis('off')

plt.savefig("multigraph.png")

plt.show()
