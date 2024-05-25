import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def generate_random_graph(num_people, file_path="graph_dataset.csv", seed=None):
    # Set the random seed
    np.random.seed(seed)
    # Initialize an empty adjacency matrix to represent the graph
    adj_matrix = np.zeros((num_people, num_people))

    # Generate random relationships
    for i in range(num_people):
        for j in range(i + 1, num_people):
            # Generate a random number between 0 and 1 to determine the strength of correlation
            strength = np.random.rand()
            
            # Assign the relationship based on the strength
            if strength < 0.1:
                # Both-sided directed edge: Strong correlation
                adj_matrix[i, j] = 1
                adj_matrix[j, i] = 1
            elif strength < 0.4:
                # One-sided directed edge: Less correlation
                adj_matrix[i, j] = 1
            else:
                # No edge: No correlation
                adj_matrix[i, j] = 0
                adj_matrix[j, i] = 0

    # Save the adjacency matrix to a file
    np.savetxt(file_path, adj_matrix, delimiter=",")
    return file_path

def draw_graph(adj_matrix, nodes, top_nodes):
    # Create a directed graph object
    G = nx.DiGraph()

    # Add nodes to the graph
    G.add_nodes_from(nodes)

    # Add edges based on the adjacency matrix
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i, j] == 1 and i in nodes and j in nodes:  # Only add edges between strong relation nodes
                G.add_edge(i, j)

    # Draw the graph
    pos = nx.spring_layout(G, k=0.5)  # positions for all nodes

    # Set node colors
    node_colors = ['skyblue' if node not in top_nodes else 'red' for node in G.nodes()]

    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=700, edge_color='k', linewidths=1, font_size=15)

    # Display the graph
    plt.title("Graph Visualization")
    plt.show()

# trend
def find_top_nodes(matrix, num_nodes=10):
    strong_relations = []
    relation_counts = [0] * len(matrix)
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            if matrix[i, j] == matrix[j, i] == 1:
                strong_relations.append((i, j))
                relation_counts[i] += 1
                relation_counts[j] += 1
    
    top_nodes = sorted(range(len(relation_counts)), key=lambda i: relation_counts[i], reverse=True)[:num_nodes]
    print(f"The top {num_nodes} nodes with the greatest number of strong correlations are: {top_nodes}")
    return strong_relations, top_nodes

# # community_discovery
# # def bipartition_graph(num_people):
# num_p=4;
# def test(num_p):
#     for i in range(num_p):
        
# cont1 == cont2 == num_people 
# cont1->firstnode cont2 ke kis kis se connected hai
