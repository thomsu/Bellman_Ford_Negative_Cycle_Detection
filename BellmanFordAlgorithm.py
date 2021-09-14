from collections import defaultdict


def detect_neg_cycle(edges):
    """Given a list of vertice pairs in a directed connected graph representing edges with corresponding weights, this function returns a list of nodes that are part of a negative cycle if any"""

    nodes = {n for n, *_ in edges}
    nodes |= {n[1] for *n, _ in edges}
    num = len(nodes)
    distance = defaultdict(lambda: float('inf'))
    distance[min(nodes)] = 0

    for _ in range(num-1):
        for edge in edges:
            if distance[edge[0]] + edge[-1] < distance[edge[1]]:
                distance[edge[1]] = distance[edge[0]] + edge[-1]

    for _ in range(num-1):
        for edge in edges:
            if distance[edge[0]] + edge[-1] < distance[edge[1]]:
                distance[edge[1]] = float('-inf')

    return [k for k, v in distance.items() if v == float('-inf')]
