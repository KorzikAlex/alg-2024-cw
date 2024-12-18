"""
This file contains the implementation of a max binary heap.
"""


class MaxBinaryHeap:
    """
    This class implements a max binary heap.
    """
    def __init__(self) -> None:
        """
        Initializes a new instance of the MaxBinaryHeap class.

        This constructor sets up an empty list to represent the heap.
        """
        self.__heap: list = []

    def _parent(self, index: int) -> int:
        """
        Calculates the index of the parent node in a binary heap.

        Args:
            index (int): The index of the current node.

        Returns:
            int: The index of the parent node.
        """
        return (index - 1) // 2

    def _left_child(self, index: int) -> int:
        """
        Calculates the index of the left child node in a binary heap.

        Args:
            index (int): The index of the current node. This index is 0-based.

        Returns:
            int: The index of the left child node. If the left child does not exist,
                 returns the index of the last node in the heap.
        """
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        """
        Calculates the index of the right child node in a binary heap.

        Args:
            index (int): The index of the current node. This index is 0-based.

        Returns:
            int: The index of the right child node. If the right child does not exist,
                 returns the index of the last node in the heap.
        """
        return 2 * index + 2

    def _swap(self, i: int, j: int) -> None:
        """
        Swaps the elements at indices i and j in the heap.

        This method is used to maintain the heap property when elements are moved
        up or down the heap.

        Parameters:
        - i (int): The index of the first element to swap.
        - j (int): The index of the second element to swap.

        Returns:
        - None: This method does not return a value. It modifies the heap in-place.
        """
        self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]

    def __heapify_up(self, index: int) -> None:
        """
        Performs a heapify operation on the max heap 
        by moving the element at the given index upwards until the heap property is satisfied.

        Args:
            index (int): The index of the element to heapify upwards. This index is 0-based.

        Returns:
            None: This method does not return a value. It modifies the heap in-place.
        """
        parent: int = self._parent(index)
        if index > 0 and self.__heap[parent] < self.__heap[index]:
            self._swap(parent, index)
            self.__heapify_up(parent)

    def __heapify_down(self, index: int) -> None:
        """
        Performs a heapify operation on the max heap by moving the element 
        at the given index downwards until the heap property is satisfied.

        Args:
        - index (int): The index of the element to heapify downwards. This index is 0-based.

        Returns:
        - None: This method does not return a value. It modifies the heap in-place.

        Local Variables:
        - left (int): The index of the left child node.
        - right (int): The index of the right child node.
        - largest (int): The index of the largest node between the current node and its children.

        The method compares the values of the current node 
        and its children, and swaps the current node with the largest child if necessary. 
        The method then recursively calls itself on the largest child
        until the heap property is satisfied.
        """
        left: int = self._left_child(index)
        right: int = self._right_child(index)
        largest: int = index
        if left < len(self.__heap) and self.__heap[left] > self.__heap[largest]:
            largest = left
        if right < len(self.__heap) and self.__heap[right] > self.__heap[largest]:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self.__heapify_down(largest)


    def insert(self, value) -> None:
        """
        Inserts a new element into the priority queue.

        Args:
        - value (int or float): The value to be inserted into the priority queue.

        Returns:
        - None: This method does not return a value. It modifies the priority queue in-place.

        Raises:
        - IndexError: If the priority queue is empty, 
        attempting to insert a new element will raise an IndexError.

        This method appends the new element to the end of the heap 
        and then calls the __heapify_up method to restore the heap property. 
        The __heapify_up method moves the new element upwards in the heap 
        until the heap property is satisfied.
        """
        if type(value) != int and type(value) != float:
            raise ValueError("Value must be an integer or float.")
        self.__heap.append(value)
        self.__heapify_up(len(self.__heap) - 1)

    def extract_max(self):
        """
        Extracts and returns the maximum value from the priority queue.

        This method removes and returns the maximum value from the priority queue. If the priority
        queue is empty, it raises an IndexError. After extracting the maximum value, the method
        restores the heap property by calling the __heapify_down method.

        Parameters:
        - None: This method does not take any parameters.

        Returns:
        - float: The maximum value in the priority queue.

        Raises:
        - IndexError: If the priority queue is empty, 
        attempting to extract a maximum value will raise an IndexError.
        """
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        max_value = self.__heap[0]
        self.__heap[0] = self.__heap[-1]
        self.__heap.pop()
        self.__heapify_down(0)
        return max_value


    def peek_max(self):
        """
        Retrieves the maximum value from the priority queue without removing it.

        This method returns the maximum value in the priority queue. If the priority queue is empty,
        it raises an IndexError. The maximum value is not removed from the priority queue, so the
        priority queue remains unchanged.

        Parameters:
        - None: This method does not take any parameters.

        Returns:
        - int: The maximum value in the priority queue.

        Raises:
        - IndexError: If the priority queue is empty, 
        attempting to retrieve a maximum value will raise an IndexError.
        """
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self.__heap[0]

    def __len__(self) -> int:
        """
        Returns the number of elements in the priority queue.

        This method returns the number of elements in the priority queue. The priority queue is
        represented by a binary heap, and the length of the heap is equal to the number of elements
        in the priority queue.

        Parameters:
        - None: This method does not take any parameters.

        Returns:
        - int: The number of elements in the priority queue.
        """
        return len(self.__heap)

    def is_empty(self) -> bool:
        """
        Checks if the priority queue is empty.

        This method returns True if the priority queue is empty, and False otherwise. The priority
        queue is represented by a binary heap, and the length of the heap is equal to zero when
        the priority queue is empty.

        Parameters:
        - None: This method does not take any parameters.

        Returns:
        - bool: True if the priority queue is empty, False otherwise.
        """
        return len(self) == 0

    def __str__(self: object) -> str:
        """
        Returns a string representation of the priority queue.

        This method returns a string representation of the priority queue, where each element in the
        heap is separated by a comma and a space. The string representation is enclosed in square brackets
        and does not include any quotation marks or parentheses.

        Parameters:
        - None: This method does not take any parameters.

        Returns:
        - str: A string representation of the priority queue.
        """
        return ", ".join(map(str, self.__heap))