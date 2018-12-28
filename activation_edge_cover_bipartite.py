from graph_factory.edge_thresholds import create_bipartite_graph

graph = create_bipartite_graph(5, 2)
terminals = graph.get_terminals()
nodes = graph.get_nodes() - terminals

graph.draw(node_labels=dict(zip(nodes, 'ab')),
           save="output/stars.png")
