'''
problem statement :
Q.1) Generate a random dataset of graph(nodes=72) 
and visulize it 2d and 3d (mandatory to use seed=332)

Q.2) printing its adj matrix find popular nodes.
(mandatory to use seed=332)

Q.3) Generate a Bipartite Graph of that dataset 
visulize it with cosine similarity.

Q.4) Recommend Nodes to Node 7 and visulize it.
'''

import vish_graphs as vg
import core_rec as cs
from common_import import * 
# Q1

# Generate random graph with 72 nodes and seed 332
file_path = vg.generate_random_graph(72, seed=332)

# Load adjacency matrix
adj_matrix = np.loadtxt(file_path, delimiter=",")

# Visualize 2D graph
# vg.draw_graph(adj_matrix)

# # Visualize 3D graph (without highlighting specific nodes)
vg.draw_graph_3d(adj_matrix, None, None)


