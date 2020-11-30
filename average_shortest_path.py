import networkx as nx
import matplotlib.pyplot as plt



# print the adjacency list
"""
for line in nx.generate_adjlist(G):
    print(line)
# write edgelist to grid.edgelist
nx.write_edgelist(G, path="grid.edgelist", delimiter=":")
# read edgelist from grid.edgelist
H = nx.read_edgelist(path="grid.edgelist", delimiter=":")
"""
#nx.draw(H)
#plt.show()
two_d = []
for N in range(2, 11):

    G = nx.grid_graph([N, N])  # N * N lattice
    two_d.append(nx.average_shortest_path_length(G))

one_d = []
for N in range(2, 40):
    G = nx.grid_graph([N]) #1 * N lattice
    one_d.append(nx.average_shortest_path_length(G))

three_d = []
for N in range(2, 5):

    G = nx.grid_graph([N, N, N])  # N * N lattice
    three_d.append(nx.average_shortest_path_length(G))

plt.plot([i**3 for i in range(2, 5)], three_d)
plt.plot([i**2 for i in range(2, 11)], two_d)
plt.plot([i for i in range(2, 40)], one_d)

plt.legend(["three d lattice", "tow d lattice", "one d lattice"])
plt.xlabel("N : the number of nodes in graph")
plt.ylabel("d : average distance between nodes in graph")

plt.show()