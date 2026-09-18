# Unit 2 Discussion: Stacks and Queues

## Overview

For this assignment, I implemented stack and queue data structures in Python.
The program demonstrated how stacks use LIFO (Last In, First Out) behavior
and how queues use FIFO (First In, First Out) behavior.

I also tested empty stack and queue conditions and used real-world examples
to show how both data structures can be applied.

---

## Stack Implementation

I implemented the stack using a Python list.

The following operations were included:

- `push()` added an item to the top of the stack.
- `pop()` removed and returned the top item.
- `peek()` returned the top item without removing it.
- `is_empty()` checked whether the stack contained any items.
- `size()` returned the number of items in the stack.

The stack followed LIFO (Last In, First Out) behavior.

For example, the following actions were added:

1. Type title
2. Insert image
3. Delete paragraph
4. Change font

Because "Change font" was added last, it was removed first.

### Real-World Stack Example

I used a text editor undo history as the stack example.

This was appropriate because the most recent editing action should be undone
before earlier actions.

---

## Queue Implementation

I implemented the queue using Python's `collections.deque`.

The following operations were included:

- `enqueue()` added an item to the back of the queue.
- `dequeue()` removed and returned the item at the front.
- `front()` returned the first item without removing it.
- `is_empty()` checked whether the queue contained any items.
- `size()` returned the number of items in the queue.

The queue followed FIFO (First In, First Out) behavior.

The following support tickets were added:

1. Reset password
2. Install printer
3. Update software
4. Network issue

Because "Reset password" was added first, it was processed first.

### Real-World Queue Example

I used an IT support ticket line as the queue example.

This was appropriate because support tickets should normally be processed
in the same order in which they are received.

---

## Edge Case Handling

I tested both data structures when they were empty.

For the stack, I tested:

- `pop()` on an empty stack
- `peek()` on an empty stack

For the queue, I tested:

- `dequeue()` on an empty queue
- `front()` on an empty queue

The program handled these cases safely by displaying a clear message and
returning `None` instead of crashing.

---

## Reflection

This assignment helped me better understand the difference between stacks
and queues by implementing and testing them in Python.

I learned that a stack follows LIFO, meaning the last item added is the
first item removed. The text editor undo example helped make this behavior
clear because the most recent editing action was the first one undone.

I also learned that a queue follows FIFO, meaning the first item added is
the first item removed. The IT support ticket example demonstrated this
because the oldest ticket was processed before newer tickets.

One challenge I encountered was handling operations when the stack or queue
was empty. I solved this by checking `is_empty()` before removing or viewing
an item. This prevented the program from failing and made the output easier
to understand.

Another important lesson was that the correct data structure depends on the
order in which data needs to be processed. Stacks are useful for situations
such as undo operations and browser history, while queues are useful for
support tickets, printer jobs, and customer service lines.

Both structures require more memory as more items are added. If there are
`n` items stored, the amount of memory used grows approximately as O(n)
because each additional item requires additional storage.

Overall, this assignment improved my understanding of LIFO, FIFO, Python
classes, edge-case handling, and real-world uses of stacks and queues.