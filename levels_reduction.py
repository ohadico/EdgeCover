import random
from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx

random.seed(6)
G = nx.MultiGraph()

terminals = map(str, range(1, 3))
nodes = map(str, [3])

G.add_edge('1','3', tu=5, tv=20)
G.add_edge('1','3', tu=10, tv=10)
G.add_edge('2','3', tu=5, tv=20)
G.add_edge('2','3', tu=10, tv=10)
G.add_edge('2','3', tu=20, tv=5)

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
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, rotate=False)

plt.axis('off')
plt.savefig("output/levels_reduction.png")
plt.show()

N = nx.Graph()

terminals = ['1', '2']
nodes = ['3_5', '3_10', '3_20']
N.add_edge('1', '3_20', tu=5, tv=20)
N.add_edge('1', '3_10', tu=10, tv=10)
N.add_edge('2', '3_20', tu=5, tv=20)
N.add_edge('2', '3_10', tu=10, tv=10)
N.add_edge('2', '3_5', tu=20, tv=5)

pos = nx.bipartite_layout(N, terminals)

nodes_drawing = nx.draw_networkx_nodes(N, pos, nodelist=terminals, node_color='r')
nodes_drawing.set_edgecolor('black')
nodes_drawing = nx.draw_networkx_nodes(N, pos, nodelist=nodes, node_color='w')
nodes_drawing.set_edgecolor('black')
nx.draw_networkx_labels(G, pos, labels={n: n.split('_')[-1] for n in nodes})

nx.draw_networkx_edges(N, pos)

edge_labels = nx.get_edge_attributes(N, 'tu')
for edge, value in edge_labels.items():
    if edge[0] not in terminals:
        edge_labels.pop(edge)
        edge_labels[edge[::-1]] = value
nx.draw_networkx_edge_labels(N, pos,
                             edge_labels=edge_labels,
                             label_pos=0.9,
                             rotate=False)


plt.axis('off')
plt.savefig("output/levels_reduction_reduced.png")
plt.show()
