"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def display_inventory(title, inventory):
    """Display the current inventory in a readable format."""
    print(title)

    if not inventory:
        print("  Inventory is empty.")
        return

    for sku, quantity in inventory.items():
        print(f"  {sku} -> quantity {quantity}")


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")
    print("Scenario: Warehouse inventory lookup using SKU numbers.")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")

    # A Python dictionary behaves like a hash table.
    # Each SKU is used as a key and each quantity is stored as its value.
    # Python hashes each key to help determine where the pair is stored.
    # Insert and lookup operations are O(1) on average.

    inventory = {}

    inventory["P100"] = 15
    inventory["P200"] = 9
    inventory["P300"] = 24
    inventory["P400"] = 7
    inventory["P500"] = 31

    display_inventory("Inventory after inserting 5 items:", inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================

    print("\n=== LOOKUP OPERATIONS ===")

    # Python hashes the SKU key to locate its associated quantity quickly.
    print("Lookup P100 -> quantity", inventory["P100"])
    print("Lookup P400 -> quantity", inventory["P400"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================

    print("\n=== UPDATE OPERATIONS ===")

    display_inventory("Before updating P100:", inventory)

    # Assigning a new value to an existing key replaces its old value.
    inventory["P100"] = 20

    display_inventory("After updating P100 from 15 to 20:", inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================

    print("\n=== DELETE OPERATIONS ===")

    display_inventory("Before deleting P200:", inventory)

    # pop() removes the key-value pair and returns its previous value.
    removed_quantity = inventory.pop("P200")

    print(f"Removed P200, previous quantity was {removed_quantity}.")

    display_inventory("After deleting P200:", inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Edge case 1: safely search for a missing SKU.
    missing_lookup = inventory.get("P999")

    print("Missing SKU lookup P999 ->", missing_lookup)
    print("Explanation: get() returned None instead of causing a KeyError.")

    # Edge case 2: safely attempt to delete a missing SKU.
    size_before = len(inventory)

    missing_delete = inventory.pop("P999", None)

    size_after = len(inventory)

    print("Delete missing SKU P999 ->", missing_delete)
    print(f"Inventory size stayed {size_before} -> {size_after}.")

    # Edge case 3: lookup in an empty dictionary.
    empty_inventory = {}

    print(
        "Lookup P100 in empty inventory ->",
        empty_inventory.get("P100")
    )

    print("Explanation: the empty dictionary returned None.")

    # ===============================
    # TODO (Student): CUSTOM SCENARIO
    # ===============================

    print("\n=== CUSTOM WAREHOUSE SCENARIO ===")

    # Products below this quantity need to be restocked.
    reorder_level = 10

    print(f"Checking products with quantity below {reorder_level}:")

    low_stock_found = False

    for sku, quantity in inventory.items():
        if quantity < reorder_level:
            print(
                f"  {sku} has only {quantity} units and should be restocked."
            )
            low_stock_found = True

    if not low_stock_found:
        print("  No products currently require restocking.")

    # ===============================
    # TODO (Student): HASH TABLE PERFORMANCE
    # ===============================

    print("\n=== HASH TABLE PERFORMANCE ===")

    # A collision happens when different keys compete for the same
    # internal hash-table location.
    #
    # Python handles collisions automatically. However, many collisions
    # can require extra comparisons and reduce lookup performance.
    #
    # Dictionary insert, lookup, update, and delete operations are
    # O(1) on average.

    print(
        "Dictionary keys are hashed to guide placement in an internal table."
    )

    print(
        "Average insert, lookup, update, and delete operations are O(1)."
    )

    print(
        "A collision occurs when different keys compete for the same "
        "internal location."
    )

    print(
        "Python resolves collisions internally, but many collisions can "
        "require extra comparisons."
    )

    print(
        "As collision frequency increases, lookup performance may decrease."
    )

    print("\n=== FINAL INVENTORY ===")

    display_inventory("Stored items:", inventory)


if __name__ == "__main__":
    main()