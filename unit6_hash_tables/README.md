# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment demonstrated how Python dictionaries behaved like hash tables by storing data as key-value pairs. I used a warehouse inventory scenario in which SKU numbers were used as keys and product quantities were stored as values.

## Learning Objectives

- Insert key-value pairs into a dictionary
- Retrieve values using keys
- Update existing values
- Remove entries safely
- Handle missing keys and empty dictionaries
- Understand hashing, collisions, and average O(1) performance
- Apply dictionaries to a real-world inventory scenario

## Requirements Completed

1. Created and populated a dictionary with multiple SKU and quantity pairs.
2. Demonstrated successful lookup operations.
3. Updated an existing inventory quantity.
4. Deleted an existing inventory record.
5. Tested edge cases, including missing keys and an empty dictionary.
6. Created a warehouse restocking scenario.
7. Explained how dictionaries functioned as hash tables.
8. Explained collisions and their effect on performance.

## Discussion Board Reflection

While completing this assignment, I learned how Python dictionaries demonstrate the behavior of hash tables by storing data as key-value pairs. I used SKU numbers as keys and inventory quantities as values while practicing insertion, lookup, update, and deletion operations. I also learned that dictionary operations such as lookup, insertion, update, and deletion generally run in O(1) average time, which makes hash tables useful for applications that require fast access to data.

One challenge I encountered was handling missing keys without causing program errors. I solved this by using `get()` for safe lookups and `pop()` with a default value for safe deletion. I also tested an empty dictionary to make the program more robust.

Hash tables use a hash function to determine where key-value pairs are stored. A collision occurs when different keys compete for the same internal location. Python handles collisions internally, but frequent collisions can require additional comparisons and reduce performance. In an inventory system, hash tables are useful because SKU values provide unique identifiers and allow product quantities to be retrieved or updated quickly as the inventory grows.

## Real-World Application

The program used a warehouse inventory system as the real-world scenario. SKU numbers were used as unique keys, while quantities were stored as values.

The program also checked for products with quantities below a reorder level. This demonstrated how dictionaries could be used not only for fast lookup, but also for practical inventory management tasks such as identifying low-stock products.

## Conclusion

This assignment helped me better understand how Python dictionaries relate to hash tables. I learned how hashing supports efficient key-based access and why collision handling is important for maintaining performance and reliability in real-world software systems.