# Unit 4 Discussion: Binary Search Trees

## Overview

For this assignment, I created a Binary Search Tree (BST) program in Python using employee ID numbers.

The program demonstrated recursive insertion, searching, in-order traversal, duplicate handling, empty-tree behavior, and the effect of insertion order on BST performance.

## Design Approach

I used employee IDs as the values stored in the Binary Search Tree.

Each node stored an employee ID and references to a left child and a right child. Smaller employee IDs were placed in the left subtree, while larger employee IDs were placed in the right subtree.

This ordering allowed the program to choose which side of the tree to search instead of checking every value.

## Insertion

I implemented BST insertion using recursion.

When an empty position was reached, the program created a new node. If the new employee ID was smaller than the current node, the program continued through the left subtree. If it was larger, the program continued through the right subtree.

Duplicate employee IDs were ignored because each employee ID was treated as a unique value.

## Searching

I implemented the search operation recursively.

The program first compared the target employee ID with the current node. If the values matched, the search returned true.

If the target was smaller, only the left subtree was searched. If the target was larger, only the right subtree was searched.

This can make a balanced BST efficient because each comparison eliminates part of the remaining search space. A balanced BST can provide approximately O(log n) search performance.

## In-Order Traversal

I implemented in-order traversal using recursion.

The traversal visited the left subtree first, then the current node, and finally the right subtree.

Because smaller values were stored on the left and larger values were stored on the right, in-order traversal produced the employee IDs in sorted order.

The resulting order was:

1010, 1025, 1035, 1050, 1060, 1075, 1090

## Edge Cases

I tested an empty Binary Search Tree and confirmed that searching returned false and in-order traversal returned an empty list.

I also attempted to insert a duplicate employee ID. The duplicate was not added to the tree.

These checks helped make the program more reliable.

## BST Efficiency and Insertion Order

I learned that the performance of a Binary Search Tree depends on its shape.

When the tree is reasonably balanced, each comparison can eliminate a large part of the remaining search space. This can result in approximately O(log n) search performance.

However, I also inserted sequential values such as 1001, 1002, 1003, 1004, and 1005. Since every new value was larger than the previous value, the nodes were added mainly to the right side.

This produced a skewed tree that behaved more like a linked list. In that situation, search performance can become O(n).

## Real-World Application

I used employee record management as the real-world example.

A company could organize unique employee IDs in a Binary Search Tree and search for an employee by comparing ID numbers.

BST concepts can also be used in ordered collections, searchable records, indexing systems, and other applications where organized searching is useful.

## Reflection

While completing this assignment, I learned how Binary Search Trees organize data using left and right child nodes. I also gained more practice with recursion by implementing insertion, searching, and in-order traversal.

The recursive methods required the most attention because each method called itself on a smaller part of the tree. Breaking the process into smaller cases helped me understand when recursion stopped and which subtree was searched.

I also learned that a BST is not automatically efficient in every situation. A balanced tree can provide fast searching, but inserting already sorted values can create a skewed tree and reduce performance to O(n).

Overall, this assignment helped me understand how BST ordering, recursion, traversal, and tree shape work together to affect program performance.