from networkx import Graph
from heapq import heappush, heappop

def dijkstra3(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

                heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == "__main__":
    G = Graph()

    edges_with_weights = [
        ("A", "B", 1), ("A", "C", 3), ("A", "D", 7),
        ("B", "E", 5), ("C", "F", 4), ("D", "G", 2),
        ("E", "F", 6), ("F", "G", 3), ("G", "H", 1),
        ("H", "I", 2), ("I", "J", 3), ("J", "E", 4),
        ("E", "H", 5)
    ]

    for edge in edges_with_weights:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    paths = {vertex: dijkstra3(G, vertex) for vertex in G.nodes}

    for k, v in paths.items():
        print(f"From vertex {k}:\n\tDistances : {v}\n")
