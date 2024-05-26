import numpy as np
# import a as vg
import core_rec as cs
import vish_graphs as vg
import core_rec as cs

# for trainig
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
# Define your dataset and data loader
adj_matrix = np.array([[0, 1, 1, 0],
                       [1, 0, 1, 1],
                       [1, 1, 0, 0],
                       [0, 1, 0, 0]])
# Initialize Transformer Model
num_layers = 3
d_model = 128
num_heads = 4
d_feedforward = 256
input_dim = len(adj_matrix)  # Input dimension should match the number of nodes in the graph
model = cs.GraphTransformer(num_layers, d_model, num_heads, d_feedforward, input_dim)



dataset = cs.GraphDataset(adj_matrix)
data_loader = DataLoader(dataset, batch_size=16, shuffle=True)

# Define your loss function, optimizer, and other training parameters
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
num_epochs = 15

# Train the model
cs.train_model(model, data_loader, criterion, optimizer, num_epochs)



# Use the trained model for node recommendations
node_index = 2
node_embedding = torch.tensor(adj_matrix[node_index])  # Get the node embedding
recommendations = cs.recommend_similar_nodes(adj_matrix, node_index)
print(f"Nodes recommended for node {node_index}: {recommendations}")
vg.draw_graph_3d(adj_matrix, node_index, recommendations)

predictions = cs.predict(model, adj_matrix)
print("corr : ",predictions)