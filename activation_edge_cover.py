from graph_factory.edge_thresholds import generate_graph

graph = generate_graph(3, 2)

graph.draw(save='output/activation_edge_cover.png')
