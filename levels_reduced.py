from graph_factory.graph_converter import reduce_levels
from graph_factory.graph_generator import generate_levels_multigraph

multigraph = generate_levels_multigraph(4, 2, (5, 10, 20), 3, 10)

multigraph.draw()

graph = reduce_levels(multigraph)

graph.draw(tu=-0.02, tv=0.8, rotate=False,
           save='output/levels_reduced.png')
