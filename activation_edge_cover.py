from graph_factory.edge_thresholds import create_full_graph

graph = create_full_graph(3, 2)

graph.draw(save='output/activation_edge_cover.png')
