"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


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

    # Linear search checks each item sequentially from beginning to end.
    # In the worst case, all n elements must be examined.
    # Therefore, linear search has O(n) time complexity.
    for i in range(len(lst)):
        if lst[i] == target:
            return i

    # Return -1 when the target does not exist in the list.
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

    low = 0
    high = len(lst) - 1

    while low <= high:
        # Find the middle position of the remaining search range.
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid

        elif lst[mid] < target:
            # The target must be in the right half.
            # Everything at mid and to the left can be discarded.
            low = mid + 1

        else:
            # The target must be in the left half.
            # Everything at mid and to the right can be discarded.
            high = mid - 1

    # Return -1 when the target does not exist.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

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

    # A small sorted dataset was created so that both algorithms
    # could search the same collection.
    small_dataset = [10, 20, 30, 40, 50]

    print("Dataset:", small_dataset)

    # Existing value test
    print("\nSearching for existing value 30:")
    print("Linear search result:",
          linear_search(small_dataset, 30))
    print("Binary search result:",
          binary_search(small_dataset, 30))

    # Missing value test
    print("\nSearching for missing value 99:")
    print("Linear search result:",
          linear_search(small_dataset, 99))
    print("Binary search result:",
          binary_search(small_dataset, 99))

    print(
        "Both algorithms returned the same results, "
        "but they reached those results differently."
    )

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

    # A sorted dataset containing 10,000 values was created.
    large_dataset = list(range(1, 10001))
    target = 9999

    linear_result = linear_search(large_dataset, target)
    binary_result = binary_search(large_dataset, target)

    print("Dataset size:", len(large_dataset))
    print("Target:", target)
    print("Linear search result:", linear_result)
    print("Binary search result:", binary_result)

    # Linear search may need to check almost every element.
    # Binary search repeatedly divides the search range in half,
    # which gives it O(log n) time complexity.
    print(
        "Linear search is O(n) because it may inspect each value."
    )
    print(
        "Binary search is O(log n) because each comparison "
        "eliminates about half of the remaining values."
    )
    print(
        "For 10,000 sorted values, binary search requires "
        "far fewer comparisons than linear search."
    )

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

    # Edge Case 1: Empty list
    empty_list = []

    print("\n1. Empty list:")
    print("Linear search:", linear_search(empty_list, 5))
    print("Binary search:", binary_search(empty_list, 5))
    print(
        "Both algorithms returned -1 because there were "
        "no elements available to search."
    )

    # Edge Case 2: Single-element list
    single_list = [7]

    print("\n2. Single-element list:")
    print("Linear search:", linear_search(single_list, 7))
    print("Binary search:", binary_search(single_list, 7))
    print(
        "Both algorithms returned index 0 because the only "
        "element matched the target."
    )

    # Edge Case 3: Value at the first position
    boundary_list = [10, 20, 30, 40, 50]

    print("\n3. Target at first position:")
    print("Linear search:", linear_search(boundary_list, 10))
    print("Binary search:", binary_search(boundary_list, 10))

    # Edge Case 4: Value at the last position
    print("\n4. Target at last position:")
    print("Linear search:", linear_search(boundary_list, 50))
    print("Binary search:", binary_search(boundary_list, 50))

    print("\n=== ANALYSIS SUMMARY ===")
    print(
        "Linear search can work on either sorted or unsorted data."
    )
    print(
        "Binary search is faster for large datasets, but the data "
        "must be sorted first."
    )


if __name__ == "__main__":
    main()