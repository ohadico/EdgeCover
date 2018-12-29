from graph_factory.graph_generator import generate_levels_multigraph

multigraph = generate_levels_multigraph(2, 1, (5, 10, 20), 3, -1)

multigraph.set_bipartite(False)

multigraph.draw(rotate=False, save='output/levels_multigraph.png')
