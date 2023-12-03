import networkx as nx
import matplotlib.pyplot as plt
import random

# Function to create a graph with 10 nodes and randomly place 10 buses
def create_graph_with_buses():
    graph = nx.Graph()
    nodes = list("ABCDEFGHIJ")

    # Add nodes to the graph
    for node in nodes:
        graph.add_node(node)

    # Create random edges between nodes
    for i in range(15):
        node1, node2 = random.sample(nodes, 2)
        weight = random.randint(1, 10)  # Assigning random weights to edges
        graph.add_edge(node1, node2, weight=weight)

    # Randomly place 10 buses on edges
    bus_edges = random.sample(list(graph.edges()), 10)
    bus_positions = {edge: random.uniform(0.1, 0.9) for edge in bus_edges}

    return graph, bus_positions

# Create the graph with buses
graph, bus_positions = create_graph_with_buses()

# Visualize the graph with edge weights and bus positions
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold', arrows=True)
nx.draw_networkx_edge_labels(graph, pos, edge_labels={(u, v): d['weight'] for u, v, d in graph.edges(data=True)})

# Draw buses on the edges
for edge, position in bus_positions.items():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    x = x0 + (x1 - x0) * position
    y = y0 + (y1 - y0) * position
    plt.scatter(x, y, color='red', marker='o')

plt.title('Graph with Buses and Edge Weights')
plt.show()

# Function to find the fastest path considering bus positions
def fastest_path_with_buses(graph, start, end, bus_positions):
    updated_graph = graph.copy()
    for edge, position in bus_positions.items():
        updated_graph[edge[0]][edge[1]]['weight'] *= (1 + position)  # Update edge weight based on bus position
    return nx.shortest_path(updated_graph, start, end, weight='weight')

# Find the fastest path from 'A' to 'H' considering bus positions
fastest_path = fastest_path_with_buses(graph, 'A', 'H', bus_positions)

# Print the fastest path
print("Fastest path from A to H considering bus positions:", fastest_path)

# Visualize the fastest path on the graph
plt.figure(figsize=(10, 8))
nx.draw(graph, pos, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold', arrows=True)
nx.draw_networkx_edge_labels(graph, pos, edge_labels={(u, v): d['weight'] for u, v, d in graph.edges(data=True)})
nx.draw_networkx_edges(graph, pos, edgelist=[(fastest_path[i], fastest_path[i + 1]) for i in range(len(fastest_path) - 1)],
                       edge_color='pink', width=3.0)

# Draw buses on the edges
for edge, position in bus_positions.items():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    x = x0 + (x1 - x0) * position
    y = y0 + (y1 - y0) * position
    plt.scatter(x, y, color='red', marker='o')

plt.title('Fastest Path from A to H with Buses and Edge Weights')
plt.show()
