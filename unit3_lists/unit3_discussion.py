"""
Unit 3 Discussion: Lists
CMSC 315

This program demonstrates list operations using
a simple shopping list example.
"""


def insert_item(items, index, value):
    # TODO: Insert an item at a given index.

    # Check that the index is valid for insertion.
    if 0 <= index <= len(items):
        # Items at and after this index move one place right.
        items.insert(index, value)
        return True

    return False


def delete_item(items, index):
    # TODO: Delete an item using its index.

    # Check the index before deleting.
    if 0 <= index < len(items):
        # Items after this index move one place left.
        return items.pop(index)

    return None


def search_item(items, value):
    # TODO: Search for an item using linear search.

    # Linear search checks each item from left to right.
    for index, item in enumerate(items):
        if item == value:
            return index

    # -1 means the item was not found.
    return -1


def display_list(items):
    # Show the current list with indexes.
    if len(items) == 0:
        print("List is empty.")
        return

    for index, item in enumerate(items):
        print(index, "-", item)


def main():
    print("===========================")
    print("UNIT 3 DISCUSSION: LISTS")
    print("===========================")
    print("Scenario: Shopping List Manager")

    shopping_list = [
        "Milk",
        "Bread",
        "Eggs",
        "Rice"
    ]

    print("\nOriginal shopping list:")
    display_list(shopping_list)

    # ========================================
    # INSERTION
    # ========================================

    print("\n================")
    print("INSERTION TESTS")
    print("==================")

    # TODO: Insert at the beginning.
    print("\n1. Insert at the beginning:")

    insert_item(shopping_list, 0, "Apples")

    display_list(shopping_list)

    print(
        "Items moved to the right because "
        "Apples was inserted at index 0."
    )

    # TODO: Insert in the middle.
    print("\n2. Insert in the middle:")

    middle_index = len(shopping_list) // 2

    insert_item(
        shopping_list,
        middle_index,
        "Juice"
    )

    display_list(shopping_list)

    print(
        "Items after the middle index moved "
        "one position to the right."
    )

    # TODO: Insert at the end.
    print("\n3. Insert at the end:")

    insert_item(
        shopping_list,
        len(shopping_list),
        "Coffee"
    )

    display_list(shopping_list)

    print(
        "Adding at the end usually does not "
        "require existing items to shift."
    )

    print("\nInsertion performance:")
    print(
        "Inserting near the beginning or middle "
        "can take O(n) time because items shift."
    )
    print(
        "Adding at the end of a Python list is "
        "usually O(1) amortized."
    )

    # ========================================
    # DELETION
    # ========================================

    print("\n===============")
    print("DELETION TESTS")
    print("=================")

    # TODO: Delete from the beginning.
    print("\n1. Delete from the beginning:")

    removed = delete_item(shopping_list, 0)

    print("Removed:", removed)
    display_list(shopping_list)

    # TODO: Delete from the middle.
    print("\n2. Delete from the middle:")

    middle_index = len(shopping_list) // 2

    removed = delete_item(
        shopping_list,
        middle_index
    )

    print("Removed:", removed)
    display_list(shopping_list)

    # TODO: Delete from the end.
    print("\n3. Delete from the end:")

    removed = delete_item(
        shopping_list,
        len(shopping_list) - 1
    )

    print("Removed:", removed)
    display_list(shopping_list)

    print("\nDeletion performance:")
    print(
        "Deleting near the beginning or middle "
        "can take O(n) time because items shift left."
    )
    print(
        "Deleting the last item is usually faster "
        "because other items do not need to move."
    )

    # ========================================
    # SEARCH
    # ========================================

    print("\n=============")
    print("SEARCH TESTS")
    print("===============")

    # TODO: Search using linear search.

    print("\n1. Search for the first item:")

    result = search_item(
        shopping_list,
        "Milk"
    )

    if result != -1:
        print("Milk found at index:", result)
    else:
        print("Milk was not found.")

    print("\n2. Search for a middle item:")

    result = search_item(
        shopping_list,
        "Bread"
    )

    if result != -1:
        print("Bread found at index:", result)
    else:
        print("Bread was not found.")

    print("\n3. Search for the last item:")

    result = search_item(
        shopping_list,
        "Rice"
    )

    if result != -1:
        print("Rice found at index:", result)
    else:
        print("Rice was not found.")

    print("\n4. Search for a missing item:")

    result = search_item(
        shopping_list,
        "Pizza"
    )

    if result != -1:
        print("Pizza found at index:", result)
    else:
        print("Pizza was not found.")

    print("\nLinear search explanation:")
    print(
        "Linear search checks items one at a time "
        "from the beginning until a match is found."
    )
    print(
        "If there are n items, linear search can "
        "take O(n) time in the worst case."
    )

    # ========================================
    # EDGE CASES
    # ========================================

    print("\n================")
    print("EDGE CASE TESTS")
    print("==================")

    # TODO: Test invalid indexes and empty lists.

    print("\n1. Invalid delete index:")

    removed = delete_item(
        shopping_list,
        100
    )

    if removed is None:
        print("Index 100 is invalid. Nothing was deleted.")

    print("\n2. Invalid insert index:")

    inserted = insert_item(
        shopping_list,
        100,
        "Cookies"
    )

    if not inserted:
        print("Index 100 is invalid. Nothing was inserted.")

    print("\n3. Search for a missing value:")

    result = search_item(
        shopping_list,
        "Cheese"
    )

    if result == -1:
        print("Cheese was not found.")

    print("\n4. Delete from an empty list:")

    empty_list = []

    removed = delete_item(
        empty_list,
        0
    )

    if removed is None:
        print("The list is empty. Nothing was deleted.")

    print("\n5. Search an empty list:")

    result = search_item(
        empty_list,
        "Milk"
    )

    if result == -1:
        print("The list is empty. Milk was not found.")

    print("\n6. Insert into an empty list:")

    inserted = insert_item(
        empty_list,
        0,
        "Water"
    )

    if inserted:
        print("Water was added successfully.")

    display_list(empty_list)

    # ========================================
    # FINAL RESULT
    # ========================================

    print("\n====================")
    print("FINAL SHOPPING LIST")
    print("======================")

    display_list(shopping_list)

    print("\nProgram complete.")


if __name__ == "__main__":
    main()