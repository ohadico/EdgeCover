from graph_factory.graph_generator import generate_graph

graph = generate_graph(3, 2)

graph.draw(save='output/activation_edge_cover.png')
