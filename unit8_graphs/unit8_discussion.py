"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # Safely handle a missing starting node.
    if start not in graph:
        print(f"Start node '{start}' does not exist in the graph.")
        return []

    # A set keeps track of nodes that have already been discovered.
    # This prevents the same node from being visited repeatedly.
    visited = {start}

    # BFS uses a queue because a queue follows FIFO
    # (First In, First Out) order. This allows BFS to visit
    # all nearby nodes before moving deeper into the graph.
    queue = deque([start])

    # This list stores the order in which nodes are visited.
    traversal_order = []

    while queue:
        # Remove the node that has been waiting the longest.
        current = queue.popleft()
        traversal_order.append(current)

        print(f"Visiting: {current}")

        # Neighbors are added to the back of the queue so that
        # BFS continues exploring the graph level by level.
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                print(f"  Added to queue: {neighbor}")

    # Unlike DFS, which follows one path deeply before backtracking,
    # BFS explores all immediate neighbors before going deeper.
    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # This graph represents a streaming recommendation network.
    # Each node represents a movie.
    # Each edge represents a relationship such as a shared genre,
    # similar cast, or similar viewer preferences.
    #
    # The dictionary is an adjacency list:
    # each movie maps to a list of directly related movies.
    graph = {
        "Movie A": ["Movie B", "Movie C"],
        "Movie B": ["Movie A", "Movie D", "Movie E"],
        "Movie C": ["Movie A", "Movie F"],
        "Movie D": ["Movie B"],
        "Movie E": ["Movie B", "Movie F"],
        "Movie F": ["Movie C", "Movie E"]
    }

    print("\n=== GRAPH STRUCTURE ===")

    # Display each node and its neighboring nodes.
    for node, neighbors in graph.items():
        print(f"{node} -> {', '.join(neighbors)}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")

    start_node = "Movie A"

    print(f"\nStarting BFS from {start_node}:")
    print(
        "BFS explores the starting movie first, then its direct "
        "neighbors, followed by movies farther away."
    )

    traversal = bfs(graph, start_node)

    print("\nTraversal order:")
    print(" -> ".join(traversal))

    print(
        "\nMovie A is visited first. Movie B and Movie C are its "
        "immediate connections, so they are explored before nodes "
        "that are farther away."
    )

    # Add another movie to demonstrate how the graph and traversal
    # change when a new node and edge are introduced.
    print("\n=== UPDATED GRAPH ===")

    graph["Movie G"] = ["Movie F"]
    graph["Movie F"].append("Movie G")

    print(
        "Added Movie G and connected it to Movie F."
    )

    for node, neighbors in graph.items():
        print(f"{node} -> {', '.join(neighbors)}")

    print("\nBFS after adding Movie G:")

    updated_traversal = bfs(graph, start_node)

    print("\nUpdated traversal order:")
    print(" -> ".join(updated_traversal))

    print(
        "\nMovie G appears later in the traversal because BFS must "
        "first reach Movie F before discovering Movie G."
    )

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1:
    # Start BFS from a different node.
    print("\nEdge Case 1: Starting from Movie D")

    different_start = bfs(graph, "Movie D")

    print("Traversal order:")
    print(" -> ".join(different_start))

    print(
        "Changing the starting node changes the traversal order "
        "because BFS begins exploring from Movie D instead of Movie A."
    )

    # Edge Case 2:
    # Try to start BFS from a node that does not exist.
    print("\nEdge Case 2: Missing start node")

    missing_node_result = bfs(graph, "Movie Z")

    print("Traversal result:", missing_node_result)

    print(
        "The program safely returns an empty traversal instead of "
        "crashing when the starting node does not exist."
    )

    # Edge Case 3:
    # Demonstrate a disconnected graph.
    print("\nEdge Case 3: Disconnected graph")

    disconnected_graph = {
        "A": ["B"],
        "B": ["A", "C"],
        "C": ["B"],
        "D": []
    }

    print("Disconnected graph structure:")
    for node, neighbors in disconnected_graph.items():
        if neighbors:
            print(f"{node} -> {', '.join(neighbors)}")
        else:
            print(f"{node} -> No connections")

    disconnected_result = bfs(disconnected_graph, "A")

    print("Traversal order:")
    print(" -> ".join(disconnected_result))

    print(
        "Node D is not visited because it is disconnected from "
        "the component containing A, B, and C."
    )


if __name__ == "__main__":
    main()