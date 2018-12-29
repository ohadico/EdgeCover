from graph_factory.graph_generator import generate_facility_location_graph

graph = generate_facility_location_graph(2, 3, (5, 20), (5, 20), -1)

graph.draw(tv=-0.025, rotate=False, save="output/random_reduced.png")
