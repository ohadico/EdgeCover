from graph_factory.edge_thresholds import generate_facility_location_graph

graph = generate_facility_location_graph(3, 5, (20, 100), (1, 5), -2)
graph.draw(tu=0.03, save="output/facility_location.png")
