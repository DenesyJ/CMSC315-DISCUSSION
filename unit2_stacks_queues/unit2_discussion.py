# Unit 2 Discussion: Stacks and Queues
# CMSC 315

from collections import deque


# Stack implementation
class Stack:

    def __init__(self):
        # TODO: Create storage for stack items.
        self.items = []

    def push(self, item):
        # Add an item to the top of the stack.
        self.items.append(item)

    def pop(self):
        # Check if the stack is empty.
        if self.is_empty():
            print("Stack is empty. Nothing to pop.")
            return None

        return self.items.pop()

    def peek(self):
        # View the top item without removing it.
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None

        return self.items[-1]

    def is_empty(self):
        # Check if the stack has no items.
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the stack.
        return len(self.items)


# Queue implementation
class Queue:

    def __init__(self):
        # TODO: Create storage for queue items.
        self.items = deque()

    def enqueue(self, item):
        # Add an item to the back of the queue.
        self.items.append(item)

    def dequeue(self):
        # Check if the queue is empty.
        if self.is_empty():
            print("Queue is empty. Nothing to dequeue.")
            return None

        return self.items.popleft()

    def front(self):
        # View the first item without removing it.
        if self.is_empty():
            print("Queue is empty. Nothing at the front.")
            return None

        return self.items[0]

    def is_empty(self):
        # Check if the queue has no items.
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the queue.
        return len(self.items)


# Stack demonstration
def demonstrate_stack():

    print("\n========================================")
    print("STACK DEMONSTRATION")
    print("========================================")

    print("Scenario: Text Editor Undo History")
    print("Stack uses LIFO: Last In, First Out\n")

    stack = Stack()

    # Test empty stack.
    print("1. Testing an empty stack:")
    stack.pop()
    stack.peek()

    print("\n2. Adding actions to the stack:")

    actions = [
        "Type title",
        "Insert image",
        "Delete paragraph",
        "Change font"
    ]

    for action in actions:
        stack.push(action)
        print("Pushed:", action)

    print("\nCurrent stack:")
    print(stack.items)

    print("\nStack size:", stack.size())

    # Show the top item.
    print("\n3. Top item:")
    print(stack.peek())

    print("\nStack after peek:")
    print(stack.items)

    print("\nPeek did not remove the item.")

    # Remove items in LIFO order.
    print("\n4. Undoing actions:")

    while not stack.is_empty():
        print("Undo:", stack.pop())

    print("\nStack empty:", stack.is_empty())

    # Test empty stack again.
    print("\n5. Testing empty stack again:")
    stack.pop()
    stack.peek()

    print("\nLIFO Explanation:")
    print("Change font was added last, so it was removed first.")
    print("Type title was added first, so it was removed last.")


# Queue demonstration
def demonstrate_queue():

    print("\n========================================")
    print("QUEUE DEMONSTRATION")
    print("========================================")

    print("Scenario: IT Support Ticket Line")
    print("Queue uses FIFO: First In, First Out\n")

    queue = Queue()

    # Test empty queue.
    print("1. Testing an empty queue:")
    queue.dequeue()
    queue.front()

    print("\n2. Adding tickets to the queue:")

    tickets = [
        "Reset password",
        "Install printer",
        "Update software",
        "Network issue"
    ]

    for ticket in tickets:
        queue.enqueue(ticket)
        print("Enqueued:", ticket)

    print("\nCurrent queue:")
    print(list(queue.items))

    print("\nQueue size:", queue.size())

    # Show the first ticket.
    print("\n3. Front ticket:")
    print(queue.front())

    print("\nQueue after front:")
    print(list(queue.items))

    print("\nFront did not remove the ticket.")

    # Process items in FIFO order.
    print("\n4. Processing tickets:")

    while not queue.is_empty():
        print("Processing:", queue.dequeue())

    print("\nQueue empty:", queue.is_empty())

    # Test empty queue again.
    print("\n5. Testing empty queue again:")
    queue.dequeue()
    queue.front()

    print("\nFIFO Explanation:")
    print("Reset password was added first, so it was processed first.")
    print("Network issue was added last, so it was processed last.")


# Main program
def main():

    print("========================================")
    print("CMSC 315 - UNIT 2: STACKS AND QUEUES")
    print("========================================")

    demonstrate_stack()
    demonstrate_queue()

    print("\n========================================")
    print("PROGRAM COMPLETE")
    print("========================================")

    print("\nSummary:")
    print("- Stack uses LIFO.")
    print("- Queue uses FIFO.")
    print("- Empty stack and queue cases were tested.")
    print("- Real-world examples were demonstrated.")


if __name__ == "__main__":
    main()