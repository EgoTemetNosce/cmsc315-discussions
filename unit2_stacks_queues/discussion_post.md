# Unit 2 Initial Discussion Post

GitHub repository: **[Insert your repository or Unit 2 folder URL after committing the files.]**

For this assignment, I implemented a stack using a Python list and a queue using collections.deque. My custom scenario modeled a support desk. Incoming tickets were processed in arrival order, and processed action messages were stored in a stack so the newest history entry could be removed first. Removing an entry from history did not restore the ticket.

A stack follows LIFO because push and pop operate at the same end. The most recently added item is therefore removed first, as in a text editor’s undo feature. A queue follows FIFO because enqueue adds at the back and dequeue removes from the front, like customers waiting at a coffee shop.

I handled empty removal and inspection by raising descriptive IndexError exceptions. My demonstration caught those errors and continued. I also checked single-item transitions and verified that peek and front did not remove items. Using deque.popleft() avoided shifting the remaining queue items.

Each structure used O(n) storage for n stored references, plus container overhead and the memory occupied by its data. As more tickets or history entries were retained, memory requirements increased.
