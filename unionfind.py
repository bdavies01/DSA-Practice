# Union find is a data structure that tracks elements split into one or more disjoint sets
# Has two primary operations: find and union

# Kruskal's algorithm: given a graph with V vertices and E edges with weights, find the 
# minimum spanning tree: tree without a cycle with the least amount of edge weight. First,
# sort the edges by their weights, and for each edge if its two vertices are not part of
# an existing GROUP, create a new group with that edge. If the edge has a vertex in an 
# existing group already, add the other vertex and edge to the existing group. Repeat 
# for all edges in the graph, but do not add edges that form a cycle within existing 
# groups. If an edge has two vertices that belong to different groups (find), merge the two
# groups with UnionFind's "union" (as long as we don't create a cycle). 