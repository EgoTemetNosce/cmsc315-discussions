# Unit 2 Discussion: Stacks and Queues

## Overview
I implemented a list-backed stack and a deque-backed queue, preserved every original TODO comment, and demonstrated both structures with five numbers and a support desk scenario.

## Implementation
- Stack: push appended to the list; pop removed the last item; peek read the last item without removal.
- Queue: enqueue appended to the deque; dequeue used popleft; front read the first item without removal.
- Both structures raised descriptive IndexError exceptions for empty removal and inspection. The demonstration caught these errors so execution continued.
- I moved the starter's demonstration into main so importing the module did not run the demonstration.
- I documented that removing an action from history did not restore a processed ticket.

## Execution and Verification
I ran:
```bash
python unit2_discussion.py
```
The program finished with: **All demonstration assertions passed.**

The stack removed 50, 40, 30, 20, 10. The queue removed 10, 20, 30, 40, 50. Assertions checked these orders and verified nonremoving inspection. Additional checks covered empty pop/peek/dequeue/front, single-item transitions, duplicate queue values, a stored None value in the stack, and queue reuse after draining. The sample_output.txt file recorded the run.

## Efficiency and Memory
I used deque.popleft() to avoid the O(n) shifting required by list.pop(0). Stack push was amortized O(1); stack pop and peek were O(1). Queue enqueue, dequeue, and front were O(1). Each structure used O(n) auxiliary storage for n item references, plus container overhead. Referenced payloads also occupied memory; larger ticket descriptions required more space. Neither implementation imposed a fixed capacity, although available system memory remained a limit.

## Discussion Board Reflection
I learned how the position used for insertion and removal determined whether a structure followed LIFO or FIFO. I implemented a stack with a Python list and a queue with collections.deque. Using deque allowed removal from the front without shifting the remaining items.

One challenge was deciding how empty operations should behave. I raised descriptive IndexError exceptions instead of returning None, because None could also be a valid stored value. I caught those exceptions in the demonstration so the program continued running. I also moved the starter demonstration into main and used assertions to check ordering, inspection, and single-item transitions.

My support desk scenario connected both structures to one workflow. The queue processed tickets in arrival order, while the stack removed the latest processed history entry first. Removing history did not restore a ticket. A stack also suited a text editor’s undo sequence, while a queue suited a coffee shop line. Memory usage grew linearly with the number of stored items. This assignment helped me connect predictable ordering to practical design decisions and recognize why boundary cases needed explicit checks.

## Submission Status
The code and README were completed and the program was verified. Uploading and committing these files to GitHub, posting the repository link in LEO, and writing two peer responses remained pending.
