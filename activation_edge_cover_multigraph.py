from graph_factory.graph_generator import generate_multigraph

graph = generate_multigraph(3, 2, 2)

graph.draw(rotate=True, save='output/multigraph.png')
