from graph_factory.edge_thresholds import generate_multigraph

graph = generate_multigraph(3, 2, 2)

graph.draw(save='output/multigraph.png')
