import networkx as nx
import matplotlib.pyplot as plt
import uuid


class Node:
    def __init__(self, key):
        self.val = key
        self.id = str(uuid.uuid4())
        self.left = None
        self.right = None
        self.color = "#FFFFFF"


def add_edges(graph, node, pos, colors, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, label=node.val, color=node.color)
        colors.append(node.color)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, colors,
                      x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, colors,
                      x=r, y=y - 1, layer=layer + 1)
    return graph, colors


def draw_tree(tree_root, title="Binary Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    colors = []
    tree, colors = add_edges(tree, tree_root, pos, colors)
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(12, 8))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def dfs(node, visit_func, level=0):
    if node:
        node.color = visit_func(level)
        dfs(node.left, visit_func, level + 1)
        dfs(node.right, visit_func, level + 1)


def bfs(root, visit_func):
    queue = [(root, 0)]
    while queue:
        node, level = queue.pop(0)
        if node:
            node.color = visit_func(level)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))


def generate_color(level):
    intensity = 255 - min(level * 30, 255)
    return f"#{intensity:02x}{intensity:02x}FF"


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    dfs(root, generate_color)
    draw_tree(root, "DFS Binary Tree")

    bfs(root, generate_color)
    draw_tree(root, "BFS Binary Tree")
