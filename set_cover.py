from graph_factory.edge_thresholds import generate_facility_location_graph

graph = generate_facility_location_graph(3, 5, (1, 2), (0, 1), -7)
graph.draw(tu=0.03, save="output/set_cover.png")
