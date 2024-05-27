
# Main script
file_path = 'graph_dataset.csv'  # Assume this is the path to your graph file
adj_matrix = np.loadtxt(file_path, delimiter=",")
top_nodes = [0, 1, 2]  # Example top nodes as a list of integers

# Initialize Transformer Model
num_layers = 3
d_model = 128
num_heads = 4
d_feedforward = 256
input_dim = adj_matrix.shape[0]
model = GraphTransformer(num_layers, d_model, num_heads, d_feedforward, input_dim)

dataset = GraphDataset(adj_matrix)
data_loader = DataLoader(dataset, batch_size=16, shuffle=True)

# Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
num_epochs = 150

# Train the model
train_model(model, data_loader, criterion, optimizer, num_epochs)

# Use the trained model for node recommendations
node_index = 31
predictions = predict(model, adj_matrix, node_index, top_k=5)
print(f"Recommended nodes for node {node_index}: {predictions}")

# Draw the graph with recommended nodes highlighted
draw_graph(adj_matrix, top_nodes, recommended_nodes=predictions)

