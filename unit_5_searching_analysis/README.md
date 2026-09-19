# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compared linear search and binary search using Python. I implemented both search algorithms and tested them with small and large sorted datasets. I also tested several edge cases to demonstrate how each algorithm behaved under different conditions.

The activity demonstrated the difference between the sequential approach used by linear search and the divide-and-conquer approach used by binary search.

---

## Program File

The Python implementation was completed in:

```text
unit5_discussion.py
```

---

## Linear Search Implementation

I implemented linear search by checking each element in the list sequentially from the beginning until the target value was found.

If the target was found, the algorithm returned the index of the target. If the target was not present, the algorithm returned `-1`.

Linear search had a time complexity of **O(n)** because, in the worst case, every element in the list had to be checked before the search ended.

For example, when searching a list containing 10,000 elements for a value near the end of the list, linear search potentially examined almost all of the elements.

---

## Binary Search Implementation

I implemented binary search using a sorted list. The algorithm calculated the middle index of the current search range and compared the middle value with the target value.

When the target was greater than the middle value, the left half of the remaining list was discarded. When the target was smaller than the middle value, the right half was discarded.

This process continued until the target was found or there were no elements left to search.

Binary search had a time complexity of **O(log n)** because each iteration reduced the remaining search space by approximately half.

---

## Small Dataset Testing

I created the following small sorted dataset:

```python
[10, 20, 30, 40, 50]
```

I searched for the existing value `30`.

Both algorithms returned:

```text
Index 2
```

I also searched for the missing value `99`.

Both algorithms returned:

```text
-1
```

The results demonstrated that both algorithms produced the same correct result even though they used different search strategies.

---

## Large Dataset Testing

I created a sorted dataset containing 10,000 values:

```python
list(range(1, 10001))
```

I searched for:

```text
9999
```

Both algorithms returned:

```text
Index 9998
```

Although both algorithms returned the same result, binary search required far fewer comparisons.

Linear search could potentially examine almost all 10,000 elements because it processed values sequentially.

Binary search repeatedly reduced the search space by half. This made binary search significantly more efficient as the dataset became larger.

---

## Edge Case Testing

I tested multiple edge cases to verify that the algorithms handled unusual inputs correctly.

### Empty List

I searched an empty list for the value `5`.

Both algorithms returned:

```text
-1
```

This indicated that the value could not be found because there were no elements available to search.

### Single-Element List

I created the following list:

```python
[7]
```

I searched for `7`.

Both algorithms returned:

```text
0
```

This showed that both algorithms correctly identified the only element in the list.

### Target at the First Position

I searched the list:

```python
[10, 20, 30, 40, 50]
```

for the value `10`.

Both algorithms returned:

```text
0
```

### Target at the Last Position

I searched the same list for the value `50`.

Both algorithms returned:

```text
4
```

These tests demonstrated that both algorithms correctly handled boundary positions.

---

## Linear Search vs. Binary Search

Linear search processed elements one at a time and had a worst-case time complexity of **O(n)**.

Binary search repeatedly divided the remaining search range in half and had a time complexity of **O(log n)**.

As the dataset increased in size, binary search became much more efficient because the number of required comparisons increased very slowly compared with linear search.

However, binary search required the dataset to already be sorted.

---

## When Linear Search Was More Appropriate

Linear search remained useful when the data was unsorted or when the dataset was very small.

For example, if I had a short unsorted list of recently downloaded files, using linear search could have been more practical because sorting the entire list before performing one search would have required additional preparation.

Linear search also worked without requiring any special ordering of the data.

---

## When Binary Search Could Not Be Used

Binary search could not be reliably used on an unsorted dataset.

The algorithm depended on the values being ordered so that it could determine whether the target was located in the left or right half of the remaining search range.

If the list was not sorted, eliminating half of the data could incorrectly remove the portion containing the target.

Therefore, the data had to be sorted before binary search could be used correctly.

---

## Preparation Time vs. Search Speed

This assignment demonstrated a trade-off between preparation time and search performance.

Sorting data required additional work before searching. However, once the data had been sorted, binary search allowed repeated searches to be completed much more efficiently.

For applications where many searches were performed on the same dataset, the initial cost of organizing the data could have been worthwhile because later searches became much faster.

For small datasets or situations where only one search was required, linear search could have remained a simpler solution.

---

## Real-World Application

A real-world example of binary search could have involved searching an alphabetically sorted collection of names or products.

For example, a large sorted product catalog could have used binary search to quickly narrow the search range and locate a specific product.

A real-world example of linear search could have involved searching through a small unsorted collection, such as recently opened files or a short list of tasks.

---

## Conclusion

I implemented and tested both linear search and binary search in Python.

The testing demonstrated that both algorithms correctly found existing values and returned `-1` when values were not present.

The larger dataset demonstrated why binary search scaled better than linear search. Linear search had **O(n)** time complexity, while binary search had **O(log n)** time complexity.

I also verified that both algorithms handled empty lists, single-element lists, and boundary values correctly.

Overall, the assignment demonstrated that choosing an appropriate search algorithm depended on the size and organization of the dataset as well as the application's performance requirements.