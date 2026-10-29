"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Items at and after this index shift right to make room.
    # Beginning/middle insertion costs O(n); end insertion is amortized O(1).
    # Python clamps out-of-range insertion indices to valid endpoints.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Accept Python's negative indices, but reject indices outside the list.
    # Checking first prevents IndexError, including deletion from an empty list.
    if not isinstance(index, int) or not -len(lst) <= index < len(lst):
        return None
    # Removing near the beginning shifts later items left: O(n).
    # Removing the last item requires no shifts: O(1).
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # An unsorted list must be scanned sequentially: O(n) in the worst case.
    # Return immediately on the first match, including when duplicates exist.
    for index, item in enumerate(lst):
        if item == value:
            return index
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    # A streaming service watchlist keeps titles in the user's preferred order.
    watchlist = ["The Matrix", "Inception", "Interstellar"]
    print("Original watchlist:", watchlist)
    # Add a priority title first, another in the middle, and a final title last.
    for label, index, title in [
        ("Beginning", 0, "Arrival"),
        ("Middle", 2, "Dune"),
        ("End", 5, "Blade Runner"),
    ]:
        insert_at(watchlist, index, title)
        print(f"{label} insertion: {watchlist}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    # Remove watched titles and display both the removed title and remaining list.
    for label, index in [("Beginning", 0), ("Middle", (len(watchlist) - 1) // 2),
                         ("End", -1)]:
        removed = delete_at(watchlist, index)
        print(f"{label} deletion: removed {removed!r}; watchlist: {watchlist}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    # Report a zero-based index for a match and -1 for an absent title.
    for title in ["The Matrix", "Titanic"]:
        print(f"Search for {title!r}: index {search_value(watchlist, title)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    # Invalid deletion must return None without changing the watchlist.
    print("Invalid positive index:", delete_at(watchlist, 99), watchlist)
    print("Invalid negative index:", delete_at(watchlist, -99), watchlist)
    print("Invalid index type:", delete_at(watchlist, "first"), watchlist)
    # Empty lists allow insertion, but have no valid deletion or search result.
    empty = []
    print("Delete from empty list:", delete_at(empty, 0))
    print("Search empty list:", search_value(empty, "Arrival"))
    insert_at(empty, 0, "Arrival")
    print("Insert into empty list:", empty)
    # A one-item list returns to empty after deleting its only element.
    print("Delete only item:", delete_at(empty, 0), empty)
    # Duplicate searches return the first matching position.
    print("First duplicate index:", search_value(["Dune", "Dune"], "Dune"))



if __name__ == "__main__":
    main()