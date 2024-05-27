from common_import import *
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

    # Find the community of the given node
    node_community = None
    for community in communities:
        if isinstance(community, list):  # Ensure community is a list
            community = set(community)  # Convert community to a set for hashing
        if node in community:
            node_community = community
            break

    if node_community is None:
        return []

    # Recommend other nodes in the same community
    recommendations = [n for n in node_community if n != node]
    return recommendations


class GraphTransformer(nn.Module):
    def __init__(self, num_layers, d_model, num_heads, d_feedforward, input_dim):
        super(GraphTransformer, self).__init__()
        self.input_linear = nn.Linear(input_dim, d_model)  # Linear layer to map input_dim to d_model
        self.encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=num_heads, dim_feedforward=d_feedforward, batch_first=True)
        self.transformer_encoder = nn.TransformerEncoder(self.encoder_layer, num_layers=num_layers)
        self.output_linear = nn.Linear(d_model, 1)  # Output layer for predictions

    def forward(self, x):
        x = x.float()  
        x = self.input_linear(x)
        x = self.transformer_encoder(x)
        x = self.output_linear(x)
        return x



# Custom Dataset for Graph Data
class GraphDataset(Dataset):
    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix

    def __len__(self):
        return len(self.adj_matrix)

    def __getitem__(self, idx):
        return self.adj_matrix[idx], 0  # Dummy target

# Training Loop
def train_model(model, data_loader, criterion, optimizer, num_epochs):
    model.train()
    for epoch in range(num_epochs):
        for batch in data_loader:
            inputs, targets = batch
            inputs = inputs.float()
            targets = targets.float()

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item()}")

def predict(model, graph):
    model.eval()
    with torch.no_grad():
        input_data = torch.tensor(graph) 
        output = model(input_data.unsqueeze(0))
    return output.squeeze().numpy()


