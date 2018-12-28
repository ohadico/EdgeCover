import matplotlib.pyplot as plt
import networkx as nx

from graph_factory import create_edge_thresholds_graph_with_terminals_bipartite

graph = create_edge_thresholds_graph_with_terminals_bipartite()
G = graph.get_graph()
terminals = graph.get_terminals()
nodes = graph.get_nodes() - terminals

graph.draw(node_labels=dict(zip(nodes, 'ab')),
           save="output/stars.png")
