import networkx as nx

def create_text_grid(triples):
    """
    Creates a text-based spatial representation from a list of triples.

    Args:
        triples: A list of tuples, where each tuple represents a spatial relation 
                triple in the format (object1, relation, object2).
                Supported relations: 'left', 'right', 'above', 'below'.

    Returns:
        A string representing the text-based spatial grid.
    """

    G = nx.DiGraph()

    # Add nodes and edges to the graph
    for obj1, relation, obj2 in triples:
        G.add_node(obj1)
        G.add_node(obj2)
        G.add_edge(obj1, obj2, relation=relation)

    # Determine initial node positions (basic heuristic)
    pos = {node: (0, 0) for node in G.nodes}
    for obj1, obj2, data in G.edges(data=True):
        if data['relation'] == 'left':
            pos[obj2] = (pos[obj1][0] - 1, pos[obj1][1])
        elif data['relation'] == 'right':
            pos[obj2] = (pos[obj1][0] + 1, pos[obj1][1])
        elif data['relation'] == 'above':
            pos[obj2] = (pos[obj1][0], pos[obj1][1] + 1)
        elif data['relation'] == 'below':
            pos[obj2] = (pos[obj1][0], pos[obj1][1] - 1)

    # Find the grid dimensions
    min_x = min(x for x, _ in pos.values())
    max_x = max(x for x, _ in pos.values())
    min_y = min(y for _, y in pos.values())
    max_y = max(y for _, y in pos.values())

    # Create the grid
    grid = [[' ' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

    # Place objects in the grid
    for node, (x, y) in pos.items():
        grid[y - min_y][x - min_x] = node

    # Create the text representation
    text_grid = '\n'.join([''.join(row) for row in grid])

    return text_grid

# Example usage
triples = [
    ('A', 'left', 'B'),
    ('B', 'left', 'C'),
    ('Z', 'above', 'B'),
    ('X', 'below', 'C')
]

text_grid = create_text_grid(triples)
print(text_grid)