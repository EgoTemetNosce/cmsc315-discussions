# Unit 5 Discussion Searching and Algorithm Analysis

Author: Roman Dilone  
Course: CMSC 315 Data Structures and Analysis  
Date: November 10, 2026

## Overview

I completed the starter's linear and binary search functions and preserved all existing TODO prompts and comments. Both functions returned a zero-based index for a match and -1 for a missing target. I used an inventory lookup scenario to connect the algorithms to a practical decision.

## Implementation

I implemented linear search with a loop from the beginning to the end. It returned the first matching index and worked with unsorted data.

I implemented binary search with inclusive left and right boundaries. Each comparison either found the target or excluded the middle element and one half of the range. An empty list started with right equal to -1, so the loop was skipped safely. Binary search returned any matching index when duplicates existed.

Both functions accepted lists containing mutually comparable values. I kept sorting outside binary_search to preserve the starter's sorted-input contract and the meaning of returned indices. Callers were responsible for supplying sorted input, keeping each lookup focused on the search itself.

## Execution and verification

I ran:

python3 unit5_discussion.py

The program ended with:

All demonstration assertions passed.

I tested a seven-item sorted list with a present and missing value. I then searched lists containing 1,000, 10,000, and 100,000 elements for their final value and a missing value. Further assertions covered empty lists, single-element matches and misses, first and last positions, targets below and above the range, a missing interior target, and duplicate handling.

## Performance experiment

I used timeit.repeat with three batches of 50 searches per algorithm and dataset size. I reported the fastest batch's average time per search in microseconds. Dataset creation and sorting were excluded. The timings described one run and could vary with hardware and system load.

| Items | Target | Returned index for both | Linear microseconds | Binary microseconds |
| --- | --- | --- | --- | --- |
| 1,000 | 999 | 999 | 25.106 | 0.786 |
| 10,000 | 9,999 | 9,999 | 274.612 | 1.177 |
| 100,000 | 99,999 | 99,999 | 2938.167 | 1.412 |

I chose a last-position target to require a full linear scan. The measured linear time increased substantially as the lists grew, while the binary time increased much less. This matched the expected O(n) versus O(log n) growth for these last-position searches. A target at the first position would have let linear search finish in O(1). Both iterative algorithms used O(1) auxiliary space, excluding input storage and the sorted copy in the custom scenario.

## Inventory scenario and tradeoffs

I searched arrival-order product IDs [1042, 1005, 1090, 1011, 1075] with linear search. Product 1011 was found at index 3. I created a sorted copy for repeated catalog lookups and found the same product at index 1 using binary search. Each index referred to its own searched list.

For a single lookup in a small unsorted shipment list, linear search avoided sorting and preserved arrival order. For repeated searches, sorting once could justify faster later lookups. General comparison sorting could cost O(n log n), and maintaining sorted order added work when data changed.

Binary search required sorted data and comparisons consistent with that ordering. I explained that applying it directly to an unsorted arrival list could miss a present product. Its usual logarithmic time advantage also depended on efficient access to middle elements, as provided by a Python list. On a linked structure, locating those middle elements would add work.

## Discussion Board Reflection

I learned how linear and binary search used different strategies to locate the same value. My inventory example used linear search on product IDs recorded in arrival order and binary search on a sorted copy. Both returned an index or -1, but the index referred to the particular list searched.

The main challenge was updating binary search boundaries correctly. I excluded the middle position after an unsuccessful comparison so the search range always shrank. I used assertions to check empty lists, single items, missing targets, endpoints, and duplicates.

Binary search took O(log n) time on sorted lists because each step eliminated about half the remaining candidates. Linear search could inspect all n elements. My experiment compared 1,000, 10,000, and 100,000 items and showed the different growth patterns.

Linear search remained appropriate for one lookup in a small unsorted shipment list because sorting required preparation. Binary search could not reliably search an unsorted list or values without a consistent comparison order. For repeated inventory lookups, I would prepare the sorted catalog once and account for the cost of keeping it sorted.

## Submission status

I completed and verified the code and README. Running the revised file in IntelliJ, committing both files to GitHub, posting the discussion, and writing two peer responses remained submission steps.
