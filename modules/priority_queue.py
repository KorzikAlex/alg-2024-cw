"""
This file contains the implementation of a max heap.
"""

class MaxPriorityQueue:
    """
    This class implements a max heap.
    """
    def __init__(self: object) -> None:
        """
        Initializes a new instance of the MaxPriorityQueue class.

        This method creates an empty max heap 
        to store the elements. 
        The heap is represented as a list,
        where the parent node of an element 
        at index i is at index (i-1)//2, and the left and right children
        are at indices 2*i+1 and 2*i+2, respectively.

        Parameters:
        None

        Returns:
        None
        """
        self.__heap: list = []


    def _parent(self: object, index: int) -> int:
        """
        Calculates the index of the parent node in the heap.

        This method is used to find the parent node of a given node in a max heap.
        The parent node of an element at index i is at index (i-1)//2.

        Parameters:
        index (int): The index of the node for which the parent index needs to be calculated.

        Returns:
        int: The index of the parent node in the heap.
        """
        return (index - 1) // 2


    def __left_child(self: object, index: int) -> int:
        """
        Calculates the index of the left child node in the heap.

        Parameters:
        index (int): The index of the parent node in the heap.

        Returns:
        int: The index of the left child node in the heap.
        """
        return 2 * index + 1


    def __right_child(self: object, index: int) -> int:
        """
        Calculates the index of the right child node in the heap.

        Parameters:
        index (int): The index of the parent node in the heap.

        Returns:
        int: The index of the right child node in the heap.
        """
        return 2 * index + 2


    def __swap(self: object, i: int, j: int) -> None:
        """
        Swaps the elements at indices i and j in the heap.

        This method is used to maintain the heap property after performing heap operations.
        It swaps the elements at indices i and j in the heap, and then recursively calls itself
        to ensure that the heap property is maintained for the affected nodes.

        Parameters:
        i (int): The index of the first element to be swapped.
        j (int): The index of the second element to be swapped.

        Returns:
        None
        """
        self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]


    def __heapify_up(self: object, index: int) -> None:
        """
        Restores the max heap property by moving an element up the heap.

        This method compares the element at the given index with its parent
        and swaps them if the element is greater than its parent. This process
        continues recursively until the max heap property is restored or the
        root of the heap is reached.

        Parameters:
        self (object): The instance of the MaxPriorityQueue class.
        index (int): The index of the element to start heapifying from.

        Returns:
        None
        """
        parent: int = self._parent(index)
        if index > 0 and self.__heap[parent] < self.__heap[index]:
            self.__swap(parent, index)
            self.__heapify_up(parent)


    def __heapify_down(self: object, index: int) -> None:
        """
        Restores the max heap property by moving an element down the heap.

        This method compares the element at the given index with its children
        and swaps it with the larger child if necessary. This process continues
        recursively until the max heap property is restored.

        Parameters:
        self (object): The instance of the MaxPriorityQueue class.
        index (int): The index of the element to start heapifying from.

        Returns:
        None
        """
        left: int = self.__left_child(index)
        right: int = self.__right_child(index)
        largest: int = index
        if left < len(self.__heap) and self.__heap[left] > self.__heap[largest]:
            largest = left
        if right < len(self.__heap) and self.__heap[right] > self.__heap[largest]:
            largest = right
        if largest!= index:
            self.__swap(index, largest)
            self.__heapify_down(largest)


    def insert(self: object, value) -> None:
        """
        Inserts a new value into the priority queue.

        This method adds a new element to the max heap and then restores
        the heap property by moving the new element up the heap as necessary.

        Parameters:
        self (object): The instance of the MaxPriorityQueue class.
        value (int): The value to be inserted into the priority queue.

        Returns:
        None
        """
        self.__heap.append(value)
        self.__heapify_up(len(self.__heap) - 1)


    def extract_max(self: object) -> int:
        """
        Removes and returns the maximum element from the priority queue.

        This method extracts the highest priority element (maximum value) from the max heap.
        After removal, it restructures the heap to maintain the max heap property.

        Parameters:
        self (object): The instance of the MaxPriorityQueue class.

        Returns:
        int: The maximum element (highest priority) that was removed from the priority queue.

        Raises:
        IndexError: If the priority queue is empty.
        """
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        max_value = self.__heap[0]
        self.__heap[0] = self.__heap[-1]
        self.__heap.pop()
        self.__heapify_down(0)
        return max_value


    def peek_max(self: object) -> int:
        """
        Returns the maximum element in the priority queue without removing it.

        This method retrieves the highest priority element (maximum value) from the max heap
        without modifying the heap structure. If the heap is empty, it raises an IndexError.

        Parameters:
        self (object): The instance of the MaxPriorityQueue class.

        Returns:
        int: The maximum element (highest priority) in the priority queue.

        Raises:
        IndexError: If the priority queue is empty.
        """
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self.__heap[0]


    def __len__(self: object) -> int:
        """
        Get the number of elements in the priority queue.

        This method returns the current size of the priority queue.

        Parameters:
        self (object): The instance of the MaxPriorityQueue class.

        Returns:
        int: The number of elements currently in the priority queue.
        """
        return len(self.__heap)


    def is_empty(self: object) -> bool:
        """
        Check if the priority queue is empty.

        This method determines whether the priority queue contains any elements.

        Parameters:
        self (object): The instance of the MaxPriorityQueue class.

        Returns:
        bool: True if the priority queue is empty, False otherwise.
        """
        return len(self) == 0

