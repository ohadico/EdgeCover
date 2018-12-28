from graph_factory.graph_generator import generate_levels_multigraph

graph = generate_levels_multigraph(2, 1, (5, 10, 20), 3, -1)

graph.set_bipartite(False)

graph.draw(rotate=False, save='output/levels_reduction.png')
