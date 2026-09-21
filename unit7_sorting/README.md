# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment explored two sorting algorithms: Bubble Sort and Merge Sort. I implemented both algorithms in Python and compared their behavior, efficiency, and scalability using multiple datasets and edge cases.

## Learning Objectives

- Implemented Bubble Sort using adjacent comparisons and swaps
- Implemented Merge Sort using recursion and divide-and-conquer
- Compared O(n²) and O(n log n) time complexity
- Tested sorting algorithms on multiple datasets
- Handled common sorting edge cases
- Analyzed when each algorithm is appropriate

## Bubble Sort Implementation

I implemented Bubble Sort by creating a copy of the original list and repeatedly comparing adjacent elements. When the left value was greater than the right value, the values were swapped.

I also used a `swapped` flag. If an entire pass completed without a swap, the algorithm stopped early because the list was already sorted.

Bubble Sort uses nested loops, which can require approximately n × n comparisons as the input grows. Therefore, its worst-case time complexity is O(n²). This makes Bubble Sort simple to understand but inefficient for large datasets.

## Merge Sort Implementation

I implemented Merge Sort using recursion and the divide-and-conquer strategy. The original list was repeatedly divided into smaller halves until each sublist contained zero or one element.

The smaller lists were then combined using the `merge()` function. During merging, values from the left and right lists were compared and placed into a new sorted list.

Merge Sort runs in O(n log n) time, which allows it to scale much better than Bubble Sort for large datasets. The trade-off is that Merge Sort requires additional memory to create and combine temporary lists.

## Dataset Testing

### Dataset #1

Original:

`[42, 19, 88, 7, 31, 55, 12]`

Bubble Sort result:

`[7, 12, 19, 31, 42, 55, 88]`

Merge Sort result:

`[7, 12, 19, 31, 42, 55, 88]`

Both algorithms produced the same correctly sorted result.

### Dataset #2

Original:

`[73, 5, 24, 91, 16, 44, 2, 68]`

Bubble Sort result:

`[2, 5, 16, 24, 44, 68, 73, 91]`

Merge Sort result:

`[2, 5, 16, 24, 44, 68, 73, 91]`

Both algorithms again produced the same result. However, Merge Sort is more scalable because its O(n log n) time complexity grows much more slowly than Bubble Sort's O(n²) behavior.

## Edge Cases Tested

I tested several edge cases:

1. **Empty list**  
   Both algorithms safely returned an empty list.

2. **Already sorted list**  
   Both algorithms preserved the correct order. Bubble Sort stopped early because no swaps were required.

3. **Duplicate values**  
   Both algorithms correctly sorted the values while preserving all duplicates.

4. **Reverse-sorted list**  
   Both algorithms returned the correct ascending order. This case demonstrated how Bubble Sort may require many comparisons and swaps.

## Bubble Sort vs. Merge Sort

Bubble Sort is easier to implement and can be reasonable for very small or nearly sorted datasets. However, its O(n²) time complexity makes it unsuitable for large amounts of data.

Merge Sort is more complex because it uses recursion and extra memory, but its O(n log n) performance makes it much more appropriate for large datasets and applications where predictable performance is important.

A real-world example is a streaming service that must sort thousands or millions of movies by rating, popularity, or release date. Merge Sort would be a better choice for large content lists because it scales efficiently and can preserve the relative order of equal values when implemented as a stable sort.

## Reflection

While completing this assignment, I learned how two sorting algorithms can produce the same final result while using very different strategies. Bubble Sort repeatedly compared neighboring elements, while Merge Sort divided the problem into smaller parts and then merged the sorted results.

The most challenging part was understanding the recursive process in Merge Sort. I overcame this by thinking of the algorithm in two stages: first divide the list until the pieces are very small, and then merge those pieces back together in sorted order.

The performance difference between the algorithms was also important. Bubble Sort has O(n²) complexity, so the amount of work increases quickly as the dataset grows. Merge Sort has O(n log n) complexity and therefore scales much better. I would use Bubble Sort only for small or simple datasets, while I would choose Merge Sort for larger datasets where performance and stability are more important. 