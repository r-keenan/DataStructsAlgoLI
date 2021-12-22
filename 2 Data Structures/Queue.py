# try out the Python queue functions
from collections import deque

# creates queue deque that is optimized for queues. Good for appending and popping elements to anywhere in the list.
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print(queue)

x = queue.popleft()

print(x)
print(queue)

