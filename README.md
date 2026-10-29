# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

## Completed Implementation

I created a streaming service watchlist using Python's array-based list. I kept all starter TODO prompts and comments and added comments explaining shifting, validation, and performance.

- I implemented `insert_at` with `list.insert` and demonstrated beginning, middle, and end insertion.
- I implemented `delete_at` with index validation and `list.pop`. I returned the removed value, or `None` for an invalid index. I supported valid negative indices.
- I implemented `search_value` with a sequential loop. I returned the first matching index, or `-1` when no match existed.
- I demonstrated invalid positive/negative deletion indices, a non-integer deletion index, empty-list operations, a single-item deletion, and duplicate searching.
- I used watchlist titles to demonstrate adding, removing, and locating real-world list entries.

## Execution and Verification

I ran the starter before editing; it printed placeholder messages. I then ran the completed program with Python 3 using `python unit3_discussion.py` and verified its output. I also checked the functions with assertions for insertion positions, deletion positions, invalid indices, empty lists, duplicates, and negative indexing.

The insertion examples produced six titles. The deletion examples removed Arrival, Inception, and Blade Runner. The remaining watchlist contained The Matrix, Dune, and Interstellar. Searching found The Matrix at index 0 and returned -1 for Titanic. Invalid deletions returned None without changing the list.

## Performance Analysis

I identified beginning/middle insertion and deletion as O(n) because later references shifted. I identified end insertion as amortized O(1), last-item deletion as O(1), indexed access as O(1), and sequential search as O(n) in the worst case.

I compared this with a linked list: insertion or deletion could take O(1) when the relevant node and necessary links were already available. Finding the location could still take O(n). I noted that linked lists required extra link storage and usually offered poorer cache locality, while Python lists stored references in a contiguous array.

## Submission Status

I reviewed submission_checklist.md and verified the code modification, edge case, concept understanding, and customization requirements against the completed implementation. The files still needed to be uploaded and committed to GitHub, and the initial post and two peer responses still needed to be submitted in LEO.
