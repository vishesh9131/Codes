###############################################################################################################
#                                             --vishgraphs--                                                  
# vish_graph module takes adjmatrix as input and has fns like                                                
    # 1. generate_random_graph(no_of_nodes,seed=23)
    # 2. find_top_nodes(adj_matrix) : greatest number of strong correlations or famous nodes top 5 
    # 3. draw_graph draws graph(matrix,set(range(len(adj_matrix))), set )
# note: just write 3d after draw_graph this will make it in xyz space
###############################################################################################################

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import csv
import time

def loading_bar(duration, steps):
    step_duration = duration / steps
    for _ in range(steps):
        print("█", end="", flush=True)
        time.sleep(step_duration)
    print()

def generate_random_graph(num_people, file_path="graph_dataset.csv", seed=None):
    np.random.seed(seed)
    adj_matrix = np.zeros((num_people, num_people))

    loading_bar(1, 100) 
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

def draw_graph(adj_matrix, nodes, top_nodes):
    G = nx.DiGraph()

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


def draw_graph_3d(adj_matrix, nodes, top_nodes):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    pos = np.random.rand(len(nodes), 3)

    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i, j] == 1 and i in nodes and j in nodes:  # Only add edges between strong relation nodes
                ax.plot([pos[i, 0], pos[j, 0]], [pos[i, 1], pos[j, 1]], [pos[i, 2], pos[j, 2]], 'gray')

    for node in nodes:
        color = 'red' if node in top_nodes else 'black'
        ax.scatter(pos[node, 0], pos[node, 1], pos[node, 2], color=color)
    ax.text(0.95, 0.05, 0.05, 'vishGraphs_use_in_labs', fontsize=8, color='gray', ha='right', va='bottom', transform=ax.transAxes)
    plt.show()
if __name__ == "__main__":
    file_path = generate_random_graph(20, "graph_dataset.csv", seed=42)
    adj_matrix = np.loadtxt(file_path, delimiter=",")
    nodes = list(range(adj_matrix.shape[0]))
    relations, top_nodes = find_top_nodes(adj_matrix)
    draw_graph_3d(adj_matrix, nodes, top_nodes)


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


def bipartite_matrix_maker(csv_path):
    adj_matrix = []
    with open(csv_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            values = [float(value) for value in row]
            adj_matrix.append(values)
    return adj_matrix



# # community_discovery
# # def bipartition_graph(num_people):
# num_p=4;
# def test(num_p):
#     for i in range(num_p):
        
# cont1 == cont2 == num_people 
# cont1->firstnode cont2 ke kis kis se connected hai
