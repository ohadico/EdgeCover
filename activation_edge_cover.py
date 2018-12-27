from graph_factory import create_edge_thresholds_graph_with_terminals

graph = create_edge_thresholds_graph_with_terminals()

graph.draw(save='output/activation_edge_cover.png')
