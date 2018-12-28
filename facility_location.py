from graph_factory.edge_thresholds import create_facility_location

graph = create_facility_location(3, 5, (20, 100), (1, 5), -2)
graph.draw(tu=0.03, save="output/facility_location.png")
