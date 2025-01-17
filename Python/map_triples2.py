import networkx as nx
import itertools
from functools import reduce

def deconflict_save(pos, newPos, first):
    try:
        pos[list(pos.keys())[list(pos.values()).index(newPos)]] = pos[first]
        ox, oy = first
        sx, sy = newPos
        dx, dy = sx-ox, sy-oy
        for k, v in pos.items():
            x, y = v
            if x >= sx and dx > 0:
                pos[k] = (x+1, y)
            if y > sy and dy > 0:
                pos[k] = (x, y+1)
    except ValueError:
        pass
    pos[first] = newPos

def remove_repeat_predicates(triples):
    lookup, removal = [], []
    for t in triples:
        if t[1:] in lookup:
            removal.append(t) #print(t, "repeated")
        else:
            lookup.append(t[1:])
    if removal:
        print("WARNING: Removed ", ", ".join(str(r) for r in removal))
        for r in removal:
            triples.remove(r)
    
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
            fx, fy = pos[first]
            sx, sy = pos[second]
            if data['relation'] == 'above-right' and not (fx > sx and fy < sy):
                newPos = (pos[second][0] + 1, pos[second][1] - 1)
                deconflict_save(pos, newPos, first)
            elif data['relation'] == 'below-right' and not (fx > sx and fy > sy):
                newPos = (pos[second][0] + 1, pos[second][1] + 1)
                deconflict_save(pos, newPos, first)
            elif data['relation'] == 'above-left' and not (fx < sx and fy < sy):
                newPos = (pos[second][0] - 1, pos[second][1] - 1)
                deconflict_save(pos, newPos, first)
            elif data['relation'] == 'below-left' and not (fx < sx and fy > sy):
                newPos = (pos[second][0] - 1, pos[second][1] + 1)
                deconflict_save(pos, newPos, first)
            elif data['relation'] == 'left' and not (fx < sx):
                newPos = (pos[second][0] - 1, pos[second][1])
                deconflict_save(pos, newPos, first)
            elif data['relation'] == 'right' and not (fx > sx):
                newPos = (pos[second][0] + 1, pos[second][1])
                deconflict_save(pos, newPos, first)
            elif data['relation'] == 'above' and not (fy < sy):
                newPos = (pos[second][0], pos[second][1] - 1)
                deconflict_save(pos, newPos, first)
            elif data['relation'] == 'below' and not (fy > sy):
                newPos = (pos[second][0], pos[second][1] + 1)
                deconflict_save(pos, newPos, first)
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
    text_grid = '\n'.join([''.join(row) for row in grid if "".join(row).strip() != ""])

    # print(grid)
    return text_grid

# Example usage
triples = [
    ('A', 'left', 'B'),
    ('B', 'left', 'C'),
    ('Z', 'above', 'B'),
    # ('X', 'below', 'C'), # repeated commands are disliked
    ('Y', 'below-right', 'C'),
    ('R', 'right', 'A'),
    ('H', 'below-left', 'B'),
    ('U', 'right', 'B'),
    ('U', 'right', 'C'),
    ('B', 'left', 'U'),
    ('F', 'right', 'C'),
    ('D', 'left', 'C'), # breaks it, works for now
    ('P', 'below', 'C'),
    ('X', 'below', 'P'), # breaks it, works for now
    ('G', 'left', 'D'),
    ('G', 'right', 'A')
]

# repeated (_,rel,Obj) need to be axed.

text_grid = create_text_grid(triples)
print(text_grid)
