import networkx as nx
import itertools

def constraintUpdate(pos, first, second, relation):

    fx, fy = pos[first]
    sx, sy = pos[second]
    newPos = None 
    if relation == 'above-right' and (fx < sx or fy > sy):
        newPos = (pos[second][0] + 1, pos[second][1] - 1)
    elif relation == 'below-right' and (fx < sx or fy < sy):
        newPos = (pos[second][0] + 1, pos[second][1] + 1)
    elif relation == 'above-left' and (fx > sx or fy > sy):
        newPos = (pos[second][0] - 1, pos[second][1] - 1)
    elif relation == 'below-left' and (fx > sx or fy < sy):
        newPos = (pos[second][0] - 1, pos[second][1] + 1)
    elif relation == 'left' and fx > sx:
        newPos = (pos[second][0] - 1, pos[second][1])
    elif relation == 'right' and fx < sx:
        newPos = (pos[second][0] + 1, pos[second][1])
    elif relation == 'above' and fy > sy:
        newPos = (pos[second][0], pos[second][1] - 1)
    elif relation == 'below' and fy < sy:
        newPos = (pos[second][0], pos[second][1] + 1)
    else: #if newPos == ():
        return

    try: # this magic prevents elements from being overwritten in the graph
        pos[list(pos.keys())[list(pos.values()).index(newPos)]] = pos[first]
    except ValueError:
        pass
    # update element
    pos[first] = newPos

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
            print(pos[first], first)
            constraintUpdate(pos, first, second, data['relation'])
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