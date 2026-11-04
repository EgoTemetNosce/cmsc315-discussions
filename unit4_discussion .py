"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

Author: Roman Dilone
Course: CMSC 315 - Data Structures and Analysis
Assignment: Unit 4 Discussion - Binary Search Trees
Date: November 4, 2026
Filename: unit4_discussion.py

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Reconnect the root after inserting into an empty or existing tree.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # A missing child is the insertion position.
        if node is None:
            return Node(value)
        # Smaller values belong left; larger values belong right.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # Equal values are ignored so this tree stores unique IDs.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # Ordering lets each comparison skip the opposite subtree.
        # This takes O(log n) in a balanced tree but O(n) in a chain.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Reaching a missing child means the value was not found.
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return
        # Left values are smaller and right values are larger.
        # Visiting left, current, right therefore produces sorted output.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")
    print("Author: Roman Dilone")
    print("Application: Employee ID Lookup")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    # Employee IDs provide a real-world lookup scenario.
    tree = BST()
    employee_ids = [1050, 1025, 1075, 1010, 1030, 1060, 1090]
    for employee_id in employee_ids:
        tree.insert(employee_id)
    print("Employee IDs inserted:", employee_ids)
    # With this balanced shape, each comparison eliminates about half
    # the remaining candidates; arbitrary insertion orders may not.
    print("Root employee ID:", tree.root.value)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    ordered = tree.inorder()
    print("Employee IDs in sorted order:", ordered)
    print("Left subtree, current ID, then right subtree.")
    assert ordered == sorted(employee_ids)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    # Two existing IDs and two missing IDs exercise both outcomes.
    for employee_id, expected in [(1010, True), (1090, True),
                                  (1000, False), (1080, False)]:
        found = tree.search(employee_id)
        print(f"Search employee {employee_id}: {found} (expected {expected})")
        assert found == expected

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    # Empty trees have no values to visit or find.
    empty = BST()
    assert empty.inorder() == []
    assert empty.search(1050) is False
    print("Empty tree: traversal = []; search = False")

    # A single node must be found and traversed correctly.
    single = BST()
    single.insert(42)
    assert single.search(42) and single.inorder() == [42]
    assert single.search(43) is False
    print("Single-node tree: found 42; missing 43 returned False")

    # Duplicate IDs do not create additional employee records.
    tree.insert(1050)
    assert tree.inorder() == ordered
    print("Duplicate employee ID 1050 was ignored.")

    # The same IDs in sorted order create a right-only chain.
    skewed = BST()
    for employee_id in sorted(employee_ids):
        skewed.insert(employee_id)
    assert skewed.inorder() == ordered
    assert skewed.search(1090)
    for label, candidate, expected_count in [
        ("Balanced tree", tree, 3),
        ("Sorted-insertion tree", skewed, 7),
    ]:
        node = candidate.root
        comparisons = 0
        while node is not None:
            comparisons += 1
            if node.value == 1090:
                break
            node = node.left if 1090 < node.value else node.right
        assert node is not None
        assert comparisons == expected_count
        print(f"{label}: searching 1090 took {comparisons} comparisons.")
    print("All demonstration assertions passed.")



if __name__ == "__main__":
    main()
