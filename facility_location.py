import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

facilities = 'ABC'
facilities_weights = (35, 85, 43)
clients = map(str, range(1, 6))

for f, w in zip(facilities, facilities_weights):
    G.add_node(f, weight=w)
for c in clients:
    G.add_node(c, weight=0)

G.add_edges_from(('1A', '3A', '3C'), weight=1)
G.add_edges_from(('1B', '2A', '4C', '5C'), weight=2)
G.add_edges_from(('2B', '4B', '5B'), weight=3)
G.add_edges_from(('2C', '4A'), weight=4)
G.add_edges_from(('3B',), weight=5)

pos = {c: (0 + (len(clients) - i - 1) / 10.0, i) for i, c in enumerate(clients)}
pos.update({f: (1 + i / 10.0, 1 + i) for i, f in enumerate(facilities)})

nx.draw(G, pos=pos, with_labels=False)
nx.draw_networkx_labels(G, pos, labels=dict(zip(facilities, facilities_weights)))
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
