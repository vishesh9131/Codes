###############################################################################################################
#                                             --vishgraphs--                                                  
# vish_graph module takes adjmatrix as input and has fns like                                                
    # 1. generate_random_graph(no_of_nodes,seed=23)
    # 2. find_top_nodes(adj_matrix) : greatest number of strong correlations or famous nodes top 5 
    # 3. draw_graph draws graph(matrix,set(range(len(adj_matrix))), set )
# note: just write 3d after draw_graph this will make it in xyz space
###############################################################################################################

import numpy as np
import vish_graphs as vg

file_path = vg.generate_random_graph(50)

adj_matrix = np.loadtxt(file_path, delimiter=",")
strong_relations, top_nodes = vg.find_top_nodes(adj_matrix)
vg.draw_graph(adj_matrix, set(range(len(adj_matrix))), top_nodes)
print(top_nodes) 

# adj_matrix1=vg.bipartite_matrix_maker(file_path)
# vg.show_bipartite_relationship(adj_matrix1)     
