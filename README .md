# Unit 4 Discussion: Binary Search Trees

Author: Roman Dilone

Course: CMSC 315 - Data Structures and Analysis

Date: November 4, 2026

## Overview

I implemented a binary search tree (BST) that stored unique employee ID numbers. I preserved the starter comments and TODO prompts and added explanations of insertion, searching, and traversal.

## Learning Objectives

I built a BST, inserted and searched recursively, performed in-order traversal, and examined how insertion order affected tree shape.

## Implementation and Real-World Application

I used employee IDs as a lookup example. Each node stored an ID and references to its left and right children. Smaller IDs went left and larger IDs went right. Duplicate IDs were ignored. The example represented finding whether an employee ID existed; it did not store full employee records.

I inserted 1050, 1025, 1075, 1010, 1030, 1060, and 1090. In-order traversal returned:

1010, 1025, 1030, 1050, 1060, 1075, 1090

## Execution and Verification

I ran the program with:

python unit4_discussion.py

Assertions verified sorted traversal, two successful searches, two unsuccessful searches, empty-tree operations, single-node behavior, duplicate handling, and searching after sorted insertion. The run ended with:

All demonstration assertions passed.

Searching for 1090 required three comparisons in the balanced example and seven in the tree built from sorted IDs. Both trees contained the same IDs and produced the same sorted traversal.

## Efficiency and Limitations

I compared the tree shapes and found that shape affected search performance. Search and insertion took O(h) time for height h: O(log n) when balanced and O(n) when skewed. Traversal took O(n) time. The nodes required O(n) storage, recursive calls required O(h) stack space, and traversal returned an additional O(n) list.

I used mutually comparable numeric IDs. Mixed incomparable types were outside this example's input contract. The implementation did not rebalance itself; a long chain could also reach Python's recursion limit. A self-balancing tree would have improved performance guarantees.

## Discussion Board Reflection

I learned how recursive insertion, searching, and in-order traversal worked together in a binary search tree. I organized employee IDs so smaller values went left and larger values went right. This ordering allowed a search to skip an entire subtree after each comparison, unlike a linear search through an unsorted list.

The most challenging part was understanding how recursive calls returned updated node references. I addressed this by assigning each insertion result back to the appropriate child reference. I also handled an empty position as the base case and ignored duplicate IDs to avoid repeated entries.

My employee lookup example demonstrated why tree shape mattered. The balanced insertion order required three comparisons to find 1090, while inserting the same IDs in sorted order required seven. This showed that a BST did not automatically guarantee fast searches. Balanced trees supported O(log n) searches, but a chain could require O(n) work.

I also tested empty trees, missing IDs, and a single-node tree. These checks helped me connect correct recursive base cases with predictable behavior. In a larger application, I would have chosen a self-balancing tree to maintain efficient searches as records changed.

## Submission Status

The Python implementation and README were completed, and the demonstration assertions passed. GitHub upload and commit, the initial discussion post, and two peer responses still required completion.
