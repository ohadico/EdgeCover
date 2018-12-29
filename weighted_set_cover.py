from graph_factory.graph_generator import generate_facility_location_graph

graph = generate_facility_location_graph(3, 5, (20, 100), (0, 1), -7)
graph.draw(tu=0.035, save="output/weighted_set_cover.png")
