# # ###############################################################################################################
# # #                                             --vishgraphs--                                                  
# # # vish_graph module takes adjmatrix as input and has fns like                                                
# #     # 1. generate_random_graph(no_of_nodes,seed=23)
# #     # 2. find_top_nodes(adj_matrix) : greatest number of strong correlations or famous nodes top 5 
# #     # 3. draw_graph draws graph(matrix,set(range(len(adj_matrix))), set )
# # # note: just write 3d after draw_graph this will make it in xyz space
# # ###############################################################################################################
import numpy as np
import a as vg
import core_rec as cs
import vish_graphs as vg
import core_rec as cs

# for trainig
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader

file_path = vg.generate_random_graph(10)
adj_matrix = np.loadtxt(file_path, delimiter=",")
strong_relations, top_nodes = vg.find_top_nodes(adj_matrix)
# vg.draw_graph_3d_large(adj_matrix, top_nodes)
print(top_nodes)

# Initialize Transformer Model
num_layers = 3
d_model = 128
num_heads = 4
d_feedforward = 256
input_dim = len(adj_matrix)  # Input dimension should match the number of nodes in the graph
model = cs.GraphTransformer(num_layers, d_model, num_heads, d_feedforward, input_dim)

# Define your dataset and data loader
dataset = cs.GraphDataset(adj_matrix)
data_loader = DataLoader(dataset, batch_size=16, shuffle=True)

# Define your loss function, optimizer, and other training parameters
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
num_epochs = 10

# Train the model
cs.train_model(model, data_loader, criterion, optimizer, num_epochs)

# Use the trained model for node recommendations
node_index = 3
node_embedding = torch.tensor(adj_matrix[node_index])  # Get the node embedding
recommendations = cs.recommend_similar_nodes(adj_matrix, node_index)
print(f"Nodes recommended for node {node_index}: {recommendations}")

vg.draw_graph_3d(adj_matrix, node_index)



# for visulization and bipartite relationship
# file_path = vg1.generate_random_graph(50)

# adj_matrix = np.loadtxt(file_path, delimiter=",")
# strong_relations, top_nodes = vg.find_top_nodes(adj_matrix)
# # vg.draw_graph_3d_large(adj_matrix, top_nodes)
# print(top_nodes) 

# # adj_matrix1=vg.bipartite_matrix_maker(file_path)
# # vg.show_bipartite_relationship(adj_matrix1)     
# # vg.show_bipartite_relationship_with_cosine(adj_matrix)
