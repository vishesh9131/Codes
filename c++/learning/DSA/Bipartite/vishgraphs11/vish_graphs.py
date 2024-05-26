# ###############################################################################################################
# #                                             --vishgraphs--                                                  
# # vish_graph module takes adjmatrix as input and has fns like                                                
#     # 1. generate_random_graph(no_of_nodes,seed=23)
#     # 2. find_top_nodes(adj_matrix) : greatest number of strong correlations or famous nodes top 5 
#     # 3. draw_graph draws graph(matrix,set(range(len(adj_matrix))), set )
# # note: just write 3d after draw_graph this will make it in xyz space
# ###############################################################################################################

import csv
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time
from sklearn.metrics.pairwise import cosine_similarity
from networkx.algorithms.community import greedy_modularity_communities
import core_rec as cs


def generate_random_graph(num_people, file_path="graph_dataset.csv", seed=None):
    np.random.seed(seed)
    adj_matrix = np.zeros((num_people, num_people))

    np.random.seed(seed)
    adj_matrix = np.zeros((num_people, num_people))

    for i in range(num_people):
        for j in range(i + 1, num_people):
            strength = np.random.rand()
            
            if strength < 0.1:
                adj_matrix[i, j] = 1
                adj_matrix[j, i] = 1
            elif strength < 0.4:
                adj_matrix[i, j] = 1
            else:
                adj_matrix[i, j] = 0
                adj_matrix[j, i] = 0

    np.savetxt(file_path, adj_matrix, delimiter=",")
    return file_path
def recommend_similar_nodes(adj_matrix, node):
    num_nodes = len(adj_matrix)

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(adj_matrix)

    # Create bipartite graph based on cosine similarity
    B = nx.Graph()
    B.add_nodes_from(range(num_nodes), bipartite=0)
    B.add_nodes_from(range(num_nodes, 2 * num_nodes), bipartite=1)

    # Add edges based on cosine similarity
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and cosine_sim[i][j] > 0:  # Only consider positive similarity
                B.add_edge(i, j + num_nodes, weight=cosine_sim[i][j])

    # Detect communities using a community detection algorithm
    communities = list(greedy_modularity_communities(B))

    # Flatten the list of communities
    flat_communities = [node for community in communities for node in community]

    # Remove duplicates while preserving order
    flat_communities = list(dict.fromkeys(flat_communities))

    # Find the community of the given node
    node_community = None
    for community in communities:
        if node in community:
            node_community = community
            break

    if node_community is None:
        return []

    # Recommend other nodes in the same community
    recommendations = [n for n in flat_communities if n != node]
    return recommendations



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
    return strong_relations, list(top_nodes)  # Convert top_nodes to a list

def draw_graph(adj_matrix, top_nodes):
    G = nx.DiGraph()
    nodes = set(range(len(adj_matrix)))

    G.add_nodes_from(nodes)

    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i, j] == 1 and i in nodes and j in nodes:  
                G.add_edge(i, j)

    pos = nx.spring_layout(G, k=0.5)  

    node_colors = ['skyblue' if node not in top_nodes else 'red' for node in G.nodes()]

    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=700, edge_color='k', linewidths=1, font_size=15)

    plt.title("Graph Visualization")
    plt.show()

def draw_graph_3d(adj_matrix, node):
    top_nodes = recommend_similar_nodes(adj_matrix, node)
    nodes = set(range(len(adj_matrix)))
    fig = plt.figure(figsize=(12, 8))
    start_time = time.time()
    ax = fig.add_subplot(111, projection='3d')

    pos = np.random.rand(len(nodes), 3)

    # Determine the number of chunks
    num_chunks = len(nodes) // 1000 + 1

    # Convert set to list
    nodes_list = list(nodes)
    chunk_legends = []

    for chunk_idx in range(num_chunks):
        start_idx = chunk_idx * 1000
        end_idx = min((chunk_idx + 1) * 1000, len(nodes))
        chunk_nodes = nodes_list[start_idx:end_idx]  # Use the list instead of the set

        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix[i])):
                if adj_matrix[i, j] == 1 and i in chunk_nodes and j in chunk_nodes:
                    ax.plot([pos[i, 0], pos[j, 0]], [pos[i, 1], pos[j, 1]], [pos[i, 2], pos[j, 2]], 'gray')

        for n in chunk_nodes:
            color = 'red' if n == node else 'blue' if n in top_nodes else 'black'
            ax.scatter(pos[n, 0], pos[n, 1], pos[n, 2], color=color)

    ax.text(0.95, 0.05, 0.05, 'vishGraphs_use_in_labs', fontsize=8, color='gray', ha='right', va='bottom', transform=ax.transAxes)
    if num_chunks > 1:
        ax.legend(chunk_legends, title='Chunks', loc='upper left')

    plt.show()

    elapsed_time = time.time() - start_time  # Calculate the elapsed time
    print(f"Time taken to process the graph: {elapsed_time:.2f} seconds")

def show_bipartite_relationship(adj_matrix):
    B = nx.Graph()

    num_nodes = len(adj_matrix)
    B.add_nodes_from(range(num_nodes), bipartite=0)

    B.add_nodes_from(range(num_nodes, 2*num_nodes), bipartite=1)

    for i in range(num_nodes):
        for j in range(num_nodes):
            if adj_matrix[i][j] == 1:  # Fix tuple indexing here
                B.add_edge(i, j+num_nodes)  # Connect node i from set 1 to node j from set 2


    pos = nx.bipartite_layout(B, nodes=range(num_nodes))
    nx.draw(B, pos, with_labels=True, node_size=500, node_color='skyblue')
    plt.title("Bipartite Relationship Visualization")
    plt.show()

def show_bipartite_relationship_with_cosine(adj_matrix):
    num_nodes = len(adj_matrix)

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(adj_matrix)

    # Create bipartite graph based on cosine similarity
    B = nx.Graph()
    B.add_nodes_from(range(num_nodes), bipartite=0)
    B.add_nodes_from(range(num_nodes, 2*num_nodes), bipartite=1)

    # Add edges based on cosine similarity
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and cosine_sim[i][j] > 0:  # Only consider positive similarity
                B.add_edge(i, j + num_nodes, weight=cosine_sim[i][j])

    # Detect communities using a community detection algorithm
    communities = list(greedy_modularity_communities(B))

    # Create a color map for the communities
    color_map = {}
    for i, community in enumerate(communities):
        for node in community:
            color_map[node] = i

    # Draw the bipartite graph with communities
    pos = nx.bipartite_layout(B, nodes=range(num_nodes))
    node_colors = [color_map.get(node, 0) for node in B.nodes()]

    nx.draw(B, pos, with_labels=True, node_size=500, node_color=node_colors, cmap=plt.cm.rainbow)
    plt.title("Bipartite Relationship Visualization with Cosine Similarity-based Communities")
    plt.show()

def bipartite_matrix_maker(csv_path):
    adj_matrix = []
    with open(csv_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            values = [float(value) for value in row]
            adj_matrix.append(values)
    return adj_matrix


#####################################################
#To Write Poetry on
#####################################################
#  community_discovery
# # def bipartition_graph(num_people):
# num_p=4;
# def test(num_p):
#     for i in range(num_p):
        
# cont1 == cont2 == num_people 
# cont1->firstnode cont2 ke kis kis se connected hai
#####################################################