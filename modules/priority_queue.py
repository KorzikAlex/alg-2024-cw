"""
This file has implementation of Priority Queue.
"""


class PriorityQueue:
    """
    This is the main class for the Priority Queue implementation.
    """

    def __init__(self: object) -> None:
        """
        Initializes a new instance of the PriorityQueue class.
        """
        self.queue = []

    def __str__(self: object) -> str:
        """
        Returns a string representation of the priority queue.

        Returns:
        str: A string containing all the elements in the priority queue, separated by spaces.
        """
        return " ".join([str(i) for i in self.queue])

    def is_empty(self: object) -> bool:
        """
        Checks if the priority queue is empty.

        Returns:
        bool: True if the priority queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def insert(self, data) -> None:
        """
        Inserts the given data into the priority queue.

        Args:
        data: The data to be inserted into the priority queue.
        """
        self.queue.append(data)

    def delete(self):
        """
        Deletes and returns the highest priority item from the priority queue.

        Returns:
        object: The highest priority item in the priority queue.
        Raises:
        IndexError: If the priority queue is empty.
        """
        try:
            max_val = 0
            for i, j in enumerate(self.queue):
                if j > self.queue[max_val]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()
