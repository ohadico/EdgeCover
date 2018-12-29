from graph_factory.graph_converter import reduce_levels

# Import levels multi graph
from custom_multigraph import multigraph

# Reduce to graph
graph = reduce_levels(multigraph)

# draw with weights as labels
graph.draw(tu=0.1, tv=-0.025, rotate=False,
           save='output/custom_multigraph_reduced.png')
