from graph_factory.graph_generator import generate_facility_location_graph

graph = generate_facility_location_graph(3, 5, (1, 2), (0, 1), -7)
graph.draw(tv=0.035, save="output/set_cover.png")
