import networkx as nx
import matplotlib.pyplot as plt

from graph_factory import create_edge_thresholds_graph_with_terminals

graph = create_edge_thresholds_graph_with_terminals()

pos = graph.get_layout()

G = graph.get_graph()
nodes_drawing = nx.draw_networkx_nodes(G, pos, nodelist=graph.get_terminals(), node_color='r')
nodes_drawing.set_edgecolor('black')
nodes_drawing = nx.draw_networkx_nodes(G, pos, nodelist=graph.get_nodes()-graph.get_terminals(), node_color='w')
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
