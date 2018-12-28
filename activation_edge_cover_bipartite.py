from graph_factory.graph_generator import generate_bipartite_graph

graph = generate_bipartite_graph(4, 4)

graph.draw(tu=0.15, tv=0.85, save="output/bipartite.png")
