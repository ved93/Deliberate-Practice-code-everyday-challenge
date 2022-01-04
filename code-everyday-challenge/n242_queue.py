
# https://www.techiedelight.com/queue-implementation-python/

# Program to demonstrate queue in Python
from collections import deque
 
if __name__ == '__main__':
 
    queue = deque()
 
    queue.append(1)     # Insert 1 into the queue
    queue.append(2)     # Insert 2 into the queue
    queue.append(3)     # Insert 3 into the queue
    queue.append(4)     # Insert 4 into the queue
 
    # Print front item of the queue
    print("The front element is", queue[0])     # 1
 
    queue.popleft()     # removing the front element (1)
    queue.popleft()     # removing the front element (2)
 
    # Print front item of the queue
    print("The front element is", queue[0])     # 3
 
    # Print the number of elements present in the queue
    print("The queue size is", len(queue))      # 2
 
    # check whether the queue is empty
    if len(queue) == 0:
        print("The queue is empty")
    else:
        print("The queue is not empty")