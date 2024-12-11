"""
The main file.
"""

from modules.priority_queue import PriorityQueue


if __name__ == "__main__":
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    print(myQueue)
    while not myQueue.is_empty():
        print(myQueue.delete())
