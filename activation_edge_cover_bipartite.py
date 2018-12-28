from graph_factory.edge_thresholds import create_bipartite_graph

graph = create_bipartite_graph(4, 4)

graph.draw(tu=0.15, tv=0.85, save="output/bipartite.png")
