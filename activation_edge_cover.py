import random

import matplotlib.pyplot as plt
import networkx as nx

random.seed(6)
G = nx.Graph()

nodes = map(str, range(1, 6))
terminals = nodes[::2]

for i, n1 in enumerate(nodes[:-1]):
    for n2 in nodes[i+1:]:
        if n1 != n2:
            G.add_edge(n1, n2, tu=random.randint(1, 10), tv=random.randint(1, 10))

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

plt.savefig("output/activation_edge_cover.png")

plt.show()
