"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # Create a copy so the original list is not modified.
    result = lst.copy()

    n = len(result)

    # Bubble Sort uses nested loops.
    # Because the loops can each run about n times,
    # the algorithm has O(n^2) time complexity in the worst case.
    for i in range(n - 1):

        swapped = False

        # After every pass, the largest unsorted value
        # moves toward the end of the list.
        for j in range(n - 1 - i):

            # Compare neighboring values.
            if result[j] > result[j + 1]:

                # Swap values when they are out of order.
                result[j], result[j + 1] = result[j + 1], result[j]

                swapped = True

        # If no swaps occurred, the list is already sorted.
        if not swapped:
            break

    return result


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # Base case:
    # A list with zero or one item is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Divide the list into two halves.
    middle = len(lst) // 2

    left_half = lst[:middle]
    right_half = lst[middle:]

    # Recursively sort both halves.
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the two sorted halves.
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """

    result = []

    left_index = 0
    right_index = 0

    # Compare values from both sorted halves.
    while left_index < len(left) and right_index < len(right):

        # Using <= also helps preserve the order of equal values.
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Append any values remaining in the left list.
    result.extend(left[left_index:])

    # Append any values remaining in the right list.
    result.extend(right[right_index:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")

    dataset1 = [42, 19, 88, 7, 31, 55, 12]

    print("Original list:")
    print(dataset1)

    bubble_result1 = bubble_sort(dataset1)
    merge_result1 = merge_sort(dataset1)

    print("\nBubble Sort result:")
    print(bubble_result1)

    print("\nMerge Sort result:")
    print(merge_result1)

    print(
        "\nBoth algorithms produced the same sorted result. "
        "Bubble Sort repeatedly compared neighboring values, while "
        "Merge Sort divided the list into smaller halves and merged "
        "them back together."
    )

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")

    dataset2 = [73, 5, 24, 91, 16, 44, 2, 68]

    print("Original list:")
    print(dataset2)

    bubble_result2 = bubble_sort(dataset2)
    merge_result2 = merge_sort(dataset2)

    print("\nBubble Sort result:")
    print(bubble_result2)

    print("\nMerge Sort result:")
    print(merge_result2)

    print(
        "\nAgain, both algorithms produced the same final order. "
        "However, Merge Sort scales better for large datasets because "
        "its time complexity is O(n log n), while Bubble Sort can require "
        "O(n^2) comparisons."
    )

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    print("\nEdge Case 1: Empty list")

    empty_list = []

    print("Original:", empty_list)
    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort:", merge_sort(empty_list))

    print(
        "Both algorithms safely returned an empty list because "
        "there were no values to sort."
    )

    # Edge Case 2: Already sorted list
    print("\nEdge Case 2: Already sorted list")

    sorted_list = [1, 2, 3, 4, 5]

    print("Original:", sorted_list)
    print("Bubble Sort:", bubble_sort(sorted_list))
    print("Merge Sort:", merge_sort(sorted_list))

    print(
        "Bubble Sort stopped early because no swaps were required. "
        "Merge Sort still divided and merged the list."
    )

    # Edge Case 3: Duplicate values
    print("\nEdge Case 3: Duplicate values")

    duplicate_list = [4, 2, 4, 1, 2, 4]

    print("Original:", duplicate_list)
    print("Bubble Sort:", bubble_sort(duplicate_list))
    print("Merge Sort:", merge_sort(duplicate_list))

    print(
        "Both algorithms correctly sorted the list while keeping "
        "all duplicate values."
    )

    # Edge Case 4: Reverse-sorted list
    print("\nEdge Case 4: Reverse-sorted list")

    reverse_list = [9, 7, 5, 3, 1]

    print("Original:", reverse_list)
    print("Bubble Sort:", bubble_sort(reverse_list))
    print("Merge Sort:", merge_sort(reverse_list))

    print(
        "A reverse-sorted list requires many comparisons and swaps "
        "for Bubble Sort, while Merge Sort continues to divide and "
        "merge efficiently."
    )

    # Summary comparison
    print("\n=== ALGORITHM COMPARISON ===")

    print(
        "Bubble Sort uses repeated adjacent comparisons and nested loops, "
        "which leads to O(n^2) time complexity for larger datasets."
    )

    print(
        "Merge Sort uses divide-and-conquer recursion and runs in "
        "O(n log n) time, which makes it much more scalable for large datasets."
    )

    print(
        "Bubble Sort is simple and can work well for small or nearly sorted data, "
        "while Merge Sort is generally preferred for larger datasets where "
        "consistent performance is important."
    )


if __name__ == "__main__":
    main()