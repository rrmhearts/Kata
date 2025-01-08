import networkx as nx

# Create a 3x4 grid graph
G = nx.grid_2d_graph(3, 4)

# Draw the graph
import matplotlib.pyplot as plt
nx.draw(G, with_labels=True)
plt.show()