import matplotlib.pyplot as plt
import networkx as nx

from graph_factory import create_edge_thresholds_graph_with_terminals_bipartite

graph = create_edge_thresholds_graph_with_terminals_bipartite()
G = graph.get_graph()
terminals = graph.get_terminals()
nodes = graph.get_nodes() - terminals

pos = nx.bipartite_layout(G, terminals)
new_pos = dict(pos)
for n in nodes:
    new_pos.pop(n)
new_pos = dict(zip(sorted(new_pos.keys(), reverse=True), sorted(new_pos.values(), key=lambda p:p[1])))
for k,v in new_pos.items():
    pos[k] = v

nodes_drawing = nx.draw_networkx_nodes(G, pos, nodelist=terminals, node_color='r')
nodes_drawing.set_edgecolor('black')
nodes_drawing = nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color='w')
nodes_drawing.set_edgecolor('black')
nx.draw_networkx_labels(G, pos, labels={'1': 'b', '2': 'a'})

nx.draw_networkx_edges(G, pos)

edge_labels = nx.get_edge_attributes(G, 'tu')
for edge_label, value in edge_labels.items():
    if edge_label[0] not in nodes:
        edge_labels.pop(edge_label)
        edge_labels[edge_label[::-1]] = value
nx.draw_networkx_edge_labels(G, pos,
                             edge_labels=edge_labels,
                             label_pos=0.1,
                             rotate=False)

edge_labels = nx.get_edge_attributes(G, 'tv')
for edge_label, value in edge_labels.items():
    if edge_label[0] not in nodes:
        edge_labels.pop(edge_label)
        edge_labels[edge_label[::-1]] = value
nx.draw_networkx_edge_labels(G, pos,
                             edge_labels=edge_labels,
                             label_pos=0.8,
                             rotate=False)

plt.axis('off')

plt.savefig("output/stars.png")

plt.show()
