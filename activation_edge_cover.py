import random
from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx

random.seed(6)
G = nx.MultiDiGraph()

nodes = map(str, range(1, 6))
terminals = map(str, range(1, 6, 2))

for n in nodes:
    G.add_node(n)

for n1 in nodes:
    for n2 in nodes:
        if n1 != n2:
            G.add_edge(n1, n2, tu=random.randint(1, 10), tv=random.randint(1, 10))
            G.add_edge(n1, n2, tu=random.randint(1, 10), tv=random.randint(1, 10))

pos = nx.spring_layout(G)
nx.draw(G, pos=pos)
nx.draw_networkx_labels(G, pos, labels={t: 'T' for t in terminals})
edge_labels = defaultdict(str)
for edge in G.edges:
    if edge[:2] in edge_labels:
        edge_labels[edge[:2]] += '\n'
    edge_labels[edge[:2]] += "{tu}:{tv}".format(**G.edges[edge])
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
