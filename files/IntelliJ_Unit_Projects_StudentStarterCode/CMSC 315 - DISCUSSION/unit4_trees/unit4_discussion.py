"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

This assignment demonstrates how a Binary Search Tree (BST)
stores, searches, and traverses values.
"""


class Node:
    def __init__(self, value):
        # Store the value contained in this node.
        self.value = value

        # Each node can have a left and right child.
        # They start as None because the node does not
        # have any children when it is first created.
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # Start with an empty Binary Search Tree.
        # The root will be assigned when the first value is inserted.
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.

        The recursive helper is used to find the correct
        position for the new value.
        """

        # Use the recursive helper to insert the value
        # and update the root reference if necessary.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Recursively insert a value into the BST.
        """

        # If the current position is empty, create a new node.
        # This becomes the correct location for the new value.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        # This ordering allows the BST to eliminate the
        # right side of the tree when searching for a smaller value.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong in the right subtree.
        # This ordering allows the BST to eliminate the
        # left side of the tree when searching for a larger value.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # If value is equal to the current node, we do not
        # insert a duplicate. This keeps this BST simple.
        return node

    def search(self, value):
        """
        Search for a value in the BST.

        Return True if the value exists and False if it does not.
        """

        # Start the recursive search at the root.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Recursively search for a value in the BST.
        """

        # If we reach an empty position, the value was not found.
        if node is None:
            return False

        # If the current node contains the value, it was found.
        if value == node.value:
            return True

        # If the target is smaller, only search the left subtree.
        # We do not need to search the right subtree because
        # BST ordering guarantees that all right-side values
        # are larger than the current node.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # If the target is larger, only search the right subtree.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        Return a list containing the values from an
        in-order traversal.
        """

        # Create an empty list to store traversal results.
        values = []

        # Recursively perform the in-order traversal.
        self._inorder_recursive(self.root, values)

        return values

    def _inorder_recursive(self, node, values):
        """
        Recursively perform an in-order traversal.
        """

        # Stop when there is no node to visit.
        if node is None:
            return

        # First visit the entire left subtree.
        self._inorder_recursive(node.left, values)

        # Then visit the current node.
        values.append(node.value)

        # Finally visit the entire right subtree.
        self._inorder_recursive(node.right, values)

        # In a BST, all values in the left subtree are smaller
        # and all values in the right subtree are larger.
        # Therefore, visiting left -> current -> right produces
        # the values in sorted order.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # BUILD A TREE
    # ===============================

    print("\n=== TREE CONSTRUCTION ===")

    # Create an empty BST.
    tree = BST()

    # Insert at least 7 values.
    # These values create both left and right subtrees.
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]

    for value in values_to_insert:
        tree.insert(value)

    # Display the values that were inserted.
    print("Values inserted:", values_to_insert)

    # A BST is efficient because each comparison tells us
    # whether to continue searching on the left or right.
    # This allows the search space to become smaller at each step.
    #
    # For a balanced BST, searching can take approximately
    # O(log n) time instead of checking every value as in
    # a linear search, which can take O(n) time.

    # ===============================
    # IN-ORDER TRAVERSAL
    # ===============================

    print("\n=== IN-ORDER TRAVERSAL ===")

    # Perform an in-order traversal.
    traversal = tree.inorder()

    # Display the traversal results.
    print("In-order traversal:", traversal)

    # In-order traversal visits:
    # left subtree -> current node -> right subtree.
    #
    # Because a BST stores smaller values on the left and
    # larger values on the right, this traversal produces
    # the values in sorted order.
    print("The values are sorted because in-order traversal")
    print("visits smaller values first, then the current value,")
    print("and finally larger values.")

    # ===============================
    # SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")

    # Search for values that exist in the tree.
    print("Search for 40:", tree.search(40))
    print("Search for 80:", tree.search(80))

    # Search for values that do not exist in the tree.
    print("Search for 25:", tree.search(25))
    print("Search for 100:", tree.search(100))

    # The searches for 40 and 80 return True because those
    # values were inserted into the tree.
    #
    # The searches for 25 and 100 return False because those
    # values were never inserted.
    #
    # BST search is often more efficient than linear search
    # because each comparison lets us ignore an entire subtree.

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Create an empty BST to demonstrate an edge case.
    empty_tree = BST()

    # Searching an empty tree should return False because
    # there is no root node to search.
    print("Search empty tree for 10:", empty_tree.search(10))

    # Traversing an empty tree should return an empty list.
    print("In-order traversal of empty tree:", empty_tree.inorder())

    # This demonstrates that the recursive methods correctly
    # handle a None root without causing an error.


if __name__ == "__main__":
    main()
