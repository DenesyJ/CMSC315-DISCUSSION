# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explored graph traversal using Breadth-First Search (BFS). I created a graph using an adjacency list and implemented BFS in Python using a queue and a visited set.

The program modeled a streaming recommendation network. Movies were represented as nodes, while relationships between similar movies were represented as edges.

## Learning Objectives

- Represented graphs using adjacency lists
- Implemented Breadth-First Search (BFS)
- Used a queue for graph traversal
- Used a visited set to prevent repeated visits
- Analyzed level-by-level graph traversal
- Tested different graph edge cases
- Compared BFS and DFS conceptually

## Implementation

I represented the graph using a Python dictionary as an adjacency list. Each movie was stored as a key, and its connected movies were stored in a list.

The BFS algorithm used a queue based on First-In, First-Out (FIFO) behavior. The starting node was added to the queue first. As each node was visited, its unvisited neighbors were added to the end of the queue. This allowed BFS to explore nodes level by level.

A visited set was used to prevent nodes from being processed more than once.

## Program Demonstration

The original graph contained six movie nodes:

- Movie A
- Movie B
- Movie C
- Movie D
- Movie E
- Movie F

Starting from Movie A, the BFS traversal was:

`Movie A -> Movie B -> Movie C -> Movie D -> Movie E -> Movie F`

I then added Movie G and connected it to Movie F.

The updated traversal was:

`Movie A -> Movie B -> Movie C -> Movie D -> Movie E -> Movie F -> Movie G`

Movie G appeared later because BFS had to reach Movie F before discovering Movie G.

## Edge Cases Tested

I tested several edge cases:

1. **Different starting node:**  
   BFS was started from Movie D to demonstrate that the traversal order changed depending on the starting vertex.

2. **Missing starting node:**  
   The program safely handled Movie Z, which did not exist in the graph, by returning an empty traversal instead of producing an error.

3. **Disconnected graph:**  
   I tested a graph where node D was disconnected from nodes A, B, and C. BFS starting from A did not visit D because no path connected it to the starting component.

## Discussion Board Reflection

While completing this assignment, I learned how graphs could represent relationships between connected objects and how Breadth-First Search explored those relationships level by level. I also learned how a queue supported FIFO processing and how a visited set prevented the same node from being processed repeatedly.

The most challenging part was making sure that neighbors were added to the queue only when they had not already been visited. I handled this by marking nodes as visited when they were added to the queue. I also tested missing and disconnected nodes to make the program more reliable.

BFS and DFS use different traversal strategies. BFS explores nearby nodes first and is useful for finding short paths in unweighted graphs, social-network connections, and recommendation systems. DFS explores one branch deeply before backtracking and can be useful for maze exploration, dependency analysis, and searching deeply nested structures. For the streaming example, BFS was appropriate because it found content related through the closest connections first.