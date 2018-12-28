from graph_factory.edge_thresholds import create_full_multigraph

graph = create_full_multigraph(3, 2, 2)

graph.draw(save='output/multigraph.png')
