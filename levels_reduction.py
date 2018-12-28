from graph_factory.graph_generator import generate_bipartite_multigraph

graph = generate_bipartite_multigraph(1, 2, 3, -1)

graph.set_bipartite(False)

graph.draw(rotate=False, save='output/levels_reduction.png')
