import pandas as pd
import networkx as nx

# Load the data
df1 = pd.read_csv('medium.tsv', sep='\t', header=None)
df2 = pd.read_csv('large.tsv', sep='\t', header=None)

# Create directed graphs
G1 = nx.DiGraph()
G2 = nx.DiGraph()

# Add edges to the directed graphs
for index, row in df1.iterrows():
    G1.add_edge(row[0], row[1])

for index, row in df2.iterrows():
    G2.add_edge(row[0], row[1])

# Convert directed graphs to undirected
U1 = G1.to_undirected()
U2 = G2.to_undirected()

# Calculate average shortest path length for each connected component in U1
average_distances_U1 = []
for C in (U1.subgraph(c).copy() for c in nx.connected_components(U1)):
    if len(C) > 1:  # Check that the component has more than one node
        avg_distance = nx.average_shortest_path_length(C)
        average_distances_U1.append(avg_distance)

# Calculate average shortest path length for each connected component in U2
average_distances_U2 = []
for C in (U2.subgraph(c).copy() for c in nx.connected_components(U2)):
    if len(C) > 1:  # Check that the component has more than one node
        avg_distance = nx.average_shortest_path_length(C)
        average_distances_U2.append(avg_distance)

# Overall average distances
overall_average_distance_U1 = sum(average_distances_U1) / len(average_distances_U1) if average_distances_U1 else float('inf')
overall_average_distance_U2 = sum(average_distances_U2) / len(average_distances_U2) if average_distances_U2 else float('inf')

# Results
results = {
    'G1': overall_average_distance_U1,
    'G2': overall_average_distance_U2,
}

print("Average Distance between Node Pairs in Largest Connected Component:")
print(results)
