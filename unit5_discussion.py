"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

Author: Roman Dilone
Course: CMSC 315 - Data Structures and Analysis
Assignment: Unit 5 Discussion - Searching and Algorithm Analysis
Date: November 10, 2026
Filename: unit5_discussion.py

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


from timeit import repeat


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # A missing target can require checking all n elements: O(n).
    # Return immediately so duplicates produce the first matching index.
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    left = 0
    right = len(lst) - 1

    # An empty list starts with right = -1 and skips this loop.
    while left <= right:
        middle = left + (right - left) // 2
        value = lst[middle]
        if value == target:
            return middle
        # Sorted order rules out the opposite half after each comparison.
        # Excluding middle also guarantees that the range shrinks.
        if value < target:
            left = middle + 1
        else:
            right = middle - 1

    # Repeated halving takes O(log n) time and O(1) extra space.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")
    print("Author: Roman Dilone")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small = [10, 20, 30, 40, 50, 60, 70]
    print("Sorted values:", small)
    # A present value returns its zero-based index; a missing value returns -1.
    for target, expected in [(40, 3), (45, -1)]:
        linear_result = linear_search(small, target)
        binary_result = binary_search(small, target)
        assert linear_result == expected
        assert binary_result == expected
        print(f"Target {target}: linear = {linear_result}, "
              f"binary = {binary_result}, expected = {expected}")

    print("Both methods found the same index; -1 indicated an absent target.")
    print("For 40, linear checked four values; binary checked the middle first.")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    # Search for the last value to exercise a full linear scan.
    # Timings exclude list construction and sorting and vary across machines.
    print("Size | Target | Linear index | Binary index | "
          "Linear us/search | Binary us/search")
    for size in (1000, 10000, 100000):
        large = list(range(size))
        target = size - 1
        linear_result = linear_search(large, target)
        binary_result = binary_search(large, target)
        assert linear_result == target
        assert binary_result == target
        assert linear_search(large, size) == -1
        assert binary_search(large, size) == -1

        # Repeat batches to reduce noise from a single short measurement.
        linear_seconds = min(repeat(
            lambda: linear_search(large, target), number=50, repeat=3
        )) / 50
        binary_seconds = min(repeat(
            lambda: binary_search(large, target), number=50, repeat=3
        )) / 50
        print(f"{size} | {target} | {linear_result} | {binary_result} | "
              f"{linear_seconds * 1_000_000:.3f} | "
              f"{binary_seconds * 1_000_000:.3f}")

    # Linear search can inspect n items; binary search halves a sorted range.
    print("Worst-case growth: linear O(n); binary O(log n).")
    print("Timings excluded preparation and can vary between runs.")
    print("Linear scanned to the last position as the lists grew.")
    print("Binary discarded half the remaining positions at each step,")
    print("so its work grew much more slowly than a full sequential scan.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    cases = [
        ("Empty list", [], 81, -1),
        ("Single element found", [81], 81, 0),
        ("Single element missing", [81], 90, -1),
        ("First position", small, 10, 0),
        ("Last position", small, 70, 6),
        ("Below minimum", small, 5, -1),
        ("Above maximum", small, 75, -1),
        ("Missing between values", small, 35, -1),
    ]
    for label, values, target, expected in cases:
        linear_result = linear_search(values, target)
        binary_result = binary_search(values, target)
        assert linear_result == expected
        assert binary_result == expected
        print(f"{label}: linear = {linear_result}, "
              f"binary = {binary_result}, expected = {expected}")

    print("Empty and missing cases returned -1 because no match existed.")
    print("Single-item and endpoint cases checked safe boundary handling.")

    # Binary search may return any matching duplicate; linear returns the first.
    duplicates = [10, 20, 20, 20, 30]
    assert linear_search(duplicates, 20) == 1
    duplicate_index = binary_search(duplicates, 20)
    assert 0 <= duplicate_index < len(duplicates)
    assert duplicates[duplicate_index] == 20
    print("Duplicates: linear found the first match; binary found a valid match.")

    print("\n=== CUSTOM SCENARIO: INVENTORY LOOKUP ===")
    # Newly arrived stock is recorded in arrival order.
    incoming_ids = [1042, 1005, 1090, 1011, 1075]
    target = 1011
    arrival_index = linear_search(incoming_ids, target)
    assert arrival_index == 3
    print("Arrival-order product IDs:", incoming_ids)
    print(f"One-time linear lookup: product {target} at index {arrival_index}")

    # A sorted copy supports repeated binary lookups and preserves arrival order.
    catalog_ids = sorted(incoming_ids)
    catalog_index = binary_search(catalog_ids, target)
    assert catalog_index == 1
    print("Sorted catalog IDs:", catalog_ids)
    print(f"Binary catalog lookup: product {target} at index {catalog_index}")
    print("Each returned index refers to the list that was searched.")
    print("A one-time arrival-list search can avoid the cost of sorting.")
    print("Binary search needs sorted data with consistent comparisons.")
    print("Both functions expect lists of mutually comparable values.")
    print("\nAll demonstration assertions passed.")


if __name__ == "__main__":
    main()
