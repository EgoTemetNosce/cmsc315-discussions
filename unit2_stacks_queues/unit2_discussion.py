"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self._items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Adding and removing at the same end makes the newest item leave first.
        self._items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        # Raise an error because an empty stack has no item to remove.
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")

        return self._items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.

        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")

        # Read the newest item without changing the stack.
        return self._items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return not self._items


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self._items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        # Add at the back so earlier arrivals remain ahead of this item.
        self._items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        # Raise an error because an empty queue has no item to remove.
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")

        # Remove the oldest item without shifting all remaining items.
        return self._items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.

        if self.is_empty():
            raise IndexError("Cannot view the front of an empty queue.")

        # Read the oldest item without removing it.
        return self._items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return not self._items


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO: LIFO ===")
    stack = Stack()
    values = [10, 20, 30, 40, 50]

    # Add five values, making 50 the most recently added item.
    for value in values:
        stack.push(value)
        print(f"Pushed {value}")

    # Peek must return 50 without removing it.
    top_value = stack.peek()
    assert top_value == 50
    print(f"Peek returned {top_value} without removing it.")

    # Removing all five expected items also verifies peek preserved the stack.
    for expected in reversed(values):
        actual = stack.pop()
        print(f"Popped {actual}: newest remaining item left first")
        assert actual == expected

    assert stack.is_empty()

    # Catch empty-operation errors so the demonstration continues.
    for operation in (stack.pop, stack.peek):
        try:
            operation()
        except IndexError as error:
            print(f"Handled empty stack: {error}")
        else:
            raise AssertionError(
                "Empty stack operation should raise IndexError"
            )

    # Verify the transition from one item to an empty stack.
    stack.push(99)
    removed = stack.pop()
    assert removed == 99
    assert stack.is_empty()
    print("Single-item stack: removed 99; is_empty() = True")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO: FIFO ===")
    queue = Queue()

    # Add five values, making 10 the earliest arrival.
    for value in values:
        queue.enqueue(value)
        print(f"Enqueued {value}")

    # Front must return 10 without removing it.
    front_value = queue.front()
    assert front_value == 10
    print(f"Front returned {front_value} without removing it.")

    # Removing all five expected items also verifies front preserved the queue.
    for expected in values:
        actual = queue.dequeue()
        print(f"Dequeued {actual}: oldest remaining item left first")
        assert actual == expected

    assert queue.is_empty()

    # Catch empty-operation errors so the demonstration continues.
    for operation in (queue.dequeue, queue.front):
        try:
            operation()
        except IndexError as error:
            print(f"Handled empty queue: {error}")
        else:
            raise AssertionError(
                "Empty queue operation should raise IndexError"
            )

    # Verify the transition from one item to an empty queue.
    queue.enqueue(99)
    removed = queue.dequeue()
    assert removed == 99
    assert queue.is_empty()
    print("Single-item queue: removed 99; is_empty() = True")

    # Custom scenario: FIFO service tickets and LIFO action history.
    print("\n=== CUSTOM SCENARIO: SUPPORT DESK ===")
    tickets = Queue()
    history = Stack()

    for ticket in (
        "Reset password",
        "Install printer",
        "Update software",
    ):
        tickets.enqueue(ticket)
        print(f"Ticket arrived: {ticket}")

    # Process requests in their original arrival order.
    while not tickets.is_empty():
        ticket = tickets.dequeue()
        history.push(f"Processed ticket: {ticket}")
        print(f"FIFO service: {ticket}")

    # Remove history entries in reverse processing order.
    # This does not restore the processed tickets to the queue.
    print("LIFO history removal (did not restore tickets):")
    while not history.is_empty():
        print(f"Undo history: {history.pop()}")

    assert tickets.is_empty()
    assert history.is_empty()

    print("\n=== ADDITIONAL EDGE CASES ===")

    # None is a valid stored value, so exceptions identify empty operations.
    stack.push(None)
    assert stack.peek() is None
    assert not stack.is_empty()
    removed = stack.pop()
    assert removed is None
    assert stack.is_empty()
    print("Stored and removed None without confusing it with an empty stack.")

    # Duplicate values must remain separate queue entries.
    queue.enqueue(7)
    queue.enqueue(7)
    first = queue.dequeue()
    second = queue.dequeue()
    assert first == 7
    assert second == 7
    assert queue.is_empty()
    print("Two duplicate values were stored and removed separately.")

    # Verify a drained queue can accept and process another item.
    queue.enqueue("New request")
    assert queue.front() == "New request"
    removed = queue.dequeue()
    assert removed == "New request"
    assert queue.is_empty()
    print("The queue was successfully reused after being emptied.")

    print("\nAll demonstration assertions passed.")


if __name__ == "__main__":
    main()
