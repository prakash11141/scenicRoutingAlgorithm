import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_nodes_from([0, 1, 2, 3])

# Add edges with travel time and scenic score
G.add_edge(0, 1, travelTime=10, scenicScore=7)
G.add_edge(1, 2, travelTime=5, scenicScore=6)
G.add_edge(2, 3, travelTime=3, scenicScore=8)
G.add_edge(0, 2, travelTime=8, scenicScore=5)
G.add_edge(1, 3, travelTime=6, scenicScore=9)

# Position nodes for visualization
pos = nx.spring_layout(G)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)

# Label edges with travel time and scenic score
edge_labels = {(u, v): f"Time: {d['travelTime']}, Score: {d['scenicScore']}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

#model 1
# Shortest path based on travel time (Dijkstra)
shortest_time_path = nx.shortest_path(G, source=0, target=3, weight='travelTime')

# Calculate the total travel time of the shortest path
shortest_time = nx.shortest_path_length(G, source=0, target=3, weight='travelTime')

# Print the shortest path and total travel time
print("Shortest path (min travel time):", shortest_time_path)
print("Travel time:", shortest_time)

# Highlight the shortest path in red
path_edges = list(zip(shortest_time_path[:-1], shortest_time_path[1:]))  # Correct edge pairs for visualization
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

plt.show()


#model 2
# # Define a custom weight function for quality ratio
# def quality_ratio(u, v, d):
#     return -d['scenicScore'] / d['travelTime']  # Negative for minimization in Dijkstra
# # Calculate the best path
# best_quality_ratio_path = nx.shortest_path(G, source=0, target=3, weight=quality_ratio)
# # Calculate the total quality ratio of the best path
# best_quality_ratio = sum(G[u][v]['scenicScore'] / G[u][v]['travelTime'] for u, v in zip(best_quality_ratio_path[:-1], best_quality_ratio_path[1:]))
# # Print the results
# print("Best quality ratio path:", best_quality_ratio_path)
# print("Quality ratio:", best_quality_ratio)
# # Highlight the best path in red
# path_edges = list(zip(best_quality_ratio_path[:-1], best_quality_ratio_path[1:]))
# nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
# plt.show()



#model 3
# Scenic score maximization (negate the scenic score for shortest path search)
# best_scenic_score_path = nx.shortest_path(G, source=0, target=3, weight=lambda u, v, d: -d['scenicScore'])
# best_scenic_score = sum(G[u][v]['scenicScore'] for u, v in zip(best_scenic_score_path[:-1], best_scenic_score_path[1:]))
# print("Best scenic score path:", best_scenic_score_path)
# print("Total scenic score:", best_scenic_score)
# # Highlight the best path in red
# path_edges = list(zip(best_scenic_score_path, best_scenic_score_path[1:]))
# nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
# plt.show()