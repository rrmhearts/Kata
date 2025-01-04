import networkx as nx
import itertools

def invertSave(pos, newPos, first):
    # return None
    try:
        pos[list(pos.keys())[list(pos.values()).index(newPos)]] = pos[first]
    except ValueError:
        pass
    pos[first] = newPos

def constraintMet(pos, first, second, relation):

    fx, fy = pos[first]
    sx, sy = pos[second]
    if relation == 'above-right':
        if fx > sx and fy < sy:
            return True
        # newPos = (pos[second][0] + 1, pos[second][1] - 1)
    elif relation == 'below-right':
        if fx > sx and fy > sy:
            return True
        # newPos = (pos[second][0] + 1, pos[second][1] + 1)
    elif relation == 'above-left':
        if fx < sx and fy < sy:
            return True
        # newPos = (pos[second][0] - 1, pos[second][1] - 1)
    elif relation == 'below-left':
        if fx < sx and fy > sy:
            return True
        # newPos = (pos[second][0] - 1, pos[second][1] + 1)
    elif relation == 'left':
        if fx < sx:
            return True
        # newPos = (pos[second][0] - 1, pos[second][1])
    elif relation == 'right':
        if fx > sx:
            return True
        # newPos = (pos[second][0] + 1, pos[second][1])
    elif relation == 'above':
        if fy < sy:
            return True
        # newPos = (pos[second][0], pos[second][1] - 1)
    elif relation == 'below':
        if fy > sy:
            return True
        # newPos = (pos[second][0], pos[second][1] + 1)
    return False

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

    # Determine initial node positions (improved heuristic)
    pos = {node: (i, 0) for i, node in enumerate(G.nodes)}
    for _ in range(len(G.nodes)):
        # print(pos)
        for obj1, obj2, data in G.edges(data=True):
            first, second = obj1, obj2
            if data['relation'] == 'above-right' and not constraintMet(pos, first, second, data['relation']):
                newPos = (pos[second][0] + 1, pos[second][1] - 1)
                invertSave(pos, newPos, first)
            elif data['relation'] == 'below-right' and not constraintMet(pos, first, second, data['relation']):
                newPos = (pos[second][0] + 1, pos[second][1] + 1)
                invertSave(pos, newPos, first)
            elif data['relation'] == 'above-left' and not constraintMet(pos, first, second, data['relation']):
                newPos = (pos[second][0] - 1, pos[second][1] - 1)
                invertSave(pos, newPos, first)
            elif data['relation'] == 'below-left' and not constraintMet(pos, first, second, data['relation']):
                newPos = (pos[second][0] - 1, pos[second][1] + 1)
                invertSave(pos, newPos, first)
            elif data['relation'] == 'left' and not constraintMet(pos, first, second, data['relation']):
                newPos = (pos[second][0] - 1, pos[second][1])
                invertSave(pos, newPos, first)
            elif data['relation'] == 'right' and not constraintMet(pos, first, second, data['relation']):
                newPos = (pos[second][0] + 1, pos[second][1])
                invertSave(pos, newPos, first)
            elif data['relation'] == 'above' and not constraintMet(pos, first, second, data['relation']):
                newPos = (pos[second][0], pos[second][1] - 1)
                invertSave(pos, newPos, first)
            elif data['relation'] == 'below' and not constraintMet(pos, first, second, data['relation']):
                newPos = (pos[second][0], pos[second][1] + 1)
                invertSave(pos, newPos, first)
    print(pos)
    # for v in pos.values():
    #     if v == (-1,0):
    #         print(v)
    # for a, b in itertools.combinations(pos.values(), 2):
    #     if a == b:
    #         print(a)
    # print(pos.items())
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

    print(grid)
    return text_grid

# Example usage
triples = [
    ('A', 'left', 'B'),
    ('B', 'left', 'C'),
    ('Z', 'above', 'B'),
    ('X', 'below', 'C'),
    ('Y', 'below-right', 'C'),
    ('R', 'right', 'A'),
    ('H', 'below-left', 'B'),
    ('U', 'right', 'B'),
    ('U', 'right', 'C'),
    ('B', 'left', 'U'),
    ('F', 'right', 'C')
]

text_grid = create_text_grid(triples)
print(text_grid)