import networkx as nx
import matplotlib.pyplot as plt

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

pos = nx.bipartite_layout(G, facilities)

nodes = nx.draw_networkx_nodes(G, pos, nodelist=facilities, node_color='w')
nodes.set_edgecolor('black')
nodes = nx.draw_networkx_nodes(G, pos, nodelist=clients, node_color='r')
nodes.set_edgecolor('black')

edges = nx.draw_networkx_edges(G, pos)

for facility in facilities:
    plt.text(pos[facility][0] + 0.02, pos[facility][1] + 0.04, G.nodes[facility]['weight'])

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos,
                             edge_labels=edge_labels,
                             label_pos=0.15,
                             rotate=False)
plt.axis('off')

plt.savefig("output/facility_location.png")

plt.show()

