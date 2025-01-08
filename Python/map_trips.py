import networkx as nx
import matplotlib.pyplot as plt

def create_grid_graph(triples):
    """
    Creates a networkx grid graph from a list of spatial relation triples.

    Args:
        triples: A list of tuples, where each tuple represents a spatial relation 
                triple in the format (object1, relation, object2).
                Supported relations: 'left', 'right', 'above', 'below'.

    Returns:
        A networkx Graph object representing the spatial relations.
    """

    G = nx.Graph()

    # Add nodes to the graph
    for triple in triples:
        obj1, relation, obj2 = triple
        G.add_node(obj1)
        G.add_node(obj2)

    # Add edges based on spatial relations
    for triple in triples:
        obj1, relation, obj2 = triple
        if relation == 'left':
            G.add_edge(obj1, obj2, weight=1)  # Adjust weight for visualization if needed
        elif relation == 'right':
            G.add_edge(obj2, obj1, weight=1)
        elif relation == 'above':
            G.add_edge(obj1, obj2, weight=1)
        elif relation == 'below':
            G.add_edge(obj2, obj1, weight=1)

    return G

def visualize_graph(G):
    """
    Visualizes the given networkx graph.

    Args:
        G: The networkx Graph object to visualize.
    """

    pos = nx.spring_layout(G)  # Use spring layout for better visualization
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.show()

# Example usage
triples = [
    ('A', 'left', 'B'),
    ('B', 'left', 'C'),
    ('D', 'above', 'A'),
    ('E', 'above', 'B'),
    ('F', 'above', 'C')
]

G = create_grid_graph(triples)
visualize_graph(G)