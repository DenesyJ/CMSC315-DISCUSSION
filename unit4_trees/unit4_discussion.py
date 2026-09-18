"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREE
=========================================================

This program demonstrates a Binary Search Tree using
employee ID numbers.
"""


class TreeNode:
    def __init__(self, employee_id):
        # Store the employee ID in this node.
        self.employee_id = employee_id

        # Smaller IDs go to the left.
        self.left = None

        # Larger IDs go to the right.
        self.right = None


class EmployeeBST:
    def __init__(self):
        # The tree starts empty.
        self.root = None

    def insert(self, employee_id):
        """
        Insert an employee ID into the BST.
        """

        # TODO: Insert a value using BST ordering.
        self.root, inserted = self._insert_recursive(
            self.root,
            employee_id
        )

        return inserted

    def _insert_recursive(self, node, employee_id):
        # Create a node when an empty position is found.
        if node is None:
            return TreeNode(employee_id), True

        # Smaller values go to the left.
        if employee_id < node.employee_id:
            node.left, inserted = self._insert_recursive(
                node.left,
                employee_id
            )
            return node, inserted

        # Larger values go to the right.
        if employee_id > node.employee_id:
            node.right, inserted = self._insert_recursive(
                node.right,
                employee_id
            )
            return node, inserted

        # Duplicate IDs are not added.
        return node, False

    def search(self, employee_id):
        """
        Search for an employee ID.
        """

        # TODO: Search the BST recursively.
        return self._search_recursive(
            self.root,
            employee_id
        )

    def _search_recursive(self, node, employee_id):
        # Reaching None means the ID was not found.
        if node is None:
            return False

        # The employee ID was found.
        if employee_id == node.employee_id:
            return True

        # Smaller IDs can only be in the left subtree.
        if employee_id < node.employee_id:
            return self._search_recursive(
                node.left,
                employee_id
            )

        # Larger IDs can only be in the right subtree.
        return self._search_recursive(
            node.right,
            employee_id
        )

    def inorder(self):
        """
        Return employee IDs using in-order traversal.
        """

        # TODO: Perform an in-order traversal.
        values = []

        self._inorder_recursive(
            self.root,
            values
        )

        return values

    def _inorder_recursive(self, node, values):
        # Stop when there is no node.
        if node is None:
            return

        # Visit the left subtree first.
        self._inorder_recursive(
            node.left,
            values
        )

        # Visit the current node.
        values.append(node.employee_id)

        # Visit the right subtree last.
        self._inorder_recursive(
            node.right,
            values
        )


def main():
    print("========================================")
    print("UNIT 4 DISCUSSION: BINARY SEARCH TREE")
    print("========================================")

    print("\nScenario: Employee ID Manager")

    employee_tree = EmployeeBST()

    # ========================================
    # INSERTION
    # ========================================

    print("\n=== INSERTION TESTS ===")

    # TODO: Add several values to create both sides of the tree.
    employee_ids = [
        1050,
        1025,
        1075,
        1010,
        1035,
        1060,
        1090
    ]

    for employee_id in employee_ids:
        employee_tree.insert(employee_id)

    print("Employee IDs inserted:")
    print(employee_ids)

    print(
        "\nSmaller IDs were placed on the left "
        "and larger IDs were placed on the right."
    )

    # ========================================
    # IN-ORDER TRAVERSAL
    # ========================================

    print("\n=== IN-ORDER TRAVERSAL ===")

    sorted_ids = employee_tree.inorder()

    print("Employee IDs in sorted order:")
    print(sorted_ids)

    print(
        "In-order traversal visits the left subtree, "
        "current node, and then the right subtree."
    )

    print(
        "Because of BST ordering, this produces "
        "the values in sorted order."
    )

    # ========================================
    # SEARCH
    # ========================================

    print("\n=== SEARCH TESTS ===")

    # TODO: Search for values that exist.
    print(
        "Search for 1035:",
        employee_tree.search(1035)
    )

    print(
        "Search for 1090:",
        employee_tree.search(1090)
    )

    # TODO: Search for a value that does not exist.
    print(
        "Search for 1200:",
        employee_tree.search(1200)
    )

    print("\nSearch explanation:")

    print(
        "A BST does not need to search both sides "
        "after every comparison."
    )

    print(
        "A smaller target goes left and a larger "
        "target goes right."
    )

    print(
        "A balanced BST can search in about O(log n) time."
    )

    # ========================================
    # EDGE CASES
    # ========================================

    print("\n=== EDGE CASE TESTS ===")

    # TODO: Test an empty tree.
    empty_tree = EmployeeBST()

    print(
        "Search empty tree for 1000:",
        empty_tree.search(1000)
    )

    print(
        "Empty tree traversal:",
        empty_tree.inorder()
    )

    # TODO: Test a duplicate value.
    duplicate_added = employee_tree.insert(1050)

    print(
        "Duplicate 1050 inserted:",
        duplicate_added
    )

    print(
        "Duplicates are ignored so each employee ID "
        "appears only once."
    )

    # ========================================
    # INSERTION ORDER / PERFORMANCE
    # ========================================

    print("\n=== INSERTION ORDER TEST ===")

    skewed_tree = EmployeeBST()

    sequential_ids = [
        1001,
        1002,
        1003,
        1004,
        1005
    ]

    for employee_id in sequential_ids:
        skewed_tree.insert(employee_id)

    print(
        "Sequential IDs:",
        skewed_tree.inorder()
    )

    print(
        "Since the values were inserted in increasing order, "
        "the tree becomes skewed to the right."
    )

    print(
        "A skewed BST can have O(n) search performance, "
        "similar to a linear structure."
    )

    print("\nProgram complete.")


if __name__ == "__main__":
    main()