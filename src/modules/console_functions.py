"""
This file contains functions to work with console in meat's shop.
"""

from os import name as os_name
from os import system

from modules.max_binary_heap import MaxBinaryHeap


def clear_console() -> None:
    """
    Clears the console screen.

    This function uses the appropriate system command to clear the console
    screen based on the operating system. It uses 'cls' for Windows (nt)
    and 'clear' for Unix-based systems.

    Parameters:
    None

    Returns:
    None
    """
    system("cls" if os_name == "nt" else "clear")


def get_answer() -> int:
    """
    This function retrieves a user's choice from the console menu.

    Parameters:
    None

    Returns:
    int: The user's choice as an integer. The value must be between 1 and 4.
         If the user enters an invalid choice, a ValueError is raised.
    """
    ans = int(
        input(
            "1)Сделать поставку бройлеров в магазин\n"
            "2)Посмотреть на текущие поставки\n"
            "3)Продать бройлер максимального веса\n"
            "4)Закрыть приложение\n"
        )
    )
    if not 1 <= ans <= 4:
        raise ValueError("Answer must be between 1 and 4")
    return ans


def deliver_broilers(pq: MaxBinaryHeap) -> MaxBinaryHeap:
    """
    Adds new broilers to the shop's inventory based on user input.

    This function prompts the user to enter the weights of broilers,
    converts the input to a list of floats, and inserts each weight
    into the provided priority queue.

    Parameters:
    pq (MaxBinaryHeap): The priority queue representing the current inventory of broilers.

    Returns:
    MaxBinaryHeap: The updated priority queue with new broilers added.

    Raises:
    ValueError: If the user input cannot be converted to float values.
    """
    weights = list(map(float, input().replace(",", ".").split()))
    for i in weights:
        pq.insert(i)
    return pq


def handle_delivery(pq: MaxBinaryHeap) -> None:
    """
    Handles the delivery of broilers to the shop.

    This function manages the process of adding new broilers to the shop's inventory.
    It prompts the user to input the weights of the broilers, attempts to add them
    to the priority queue, and handles any input errors.

    Parameters:
    pq (MaxBinaryHeap): The priority queue representing the current inventory of broilers.

    Returns:
    None

    Side effects:
    - Modifies the provided MaxBinaryHeap object by adding new broiler weights.
    - Prints messages to the console for user interaction and feedback.
    - Clears the console screen during the process.
    """
    print("Сделать поставку бройлеров в магазин.\n" "Введите через пробел вес бройлеров:")
    while True:
        try:
            pq = deliver_broilers(pq)
            clear_console()
            print("Бройлеры успешно добавлены в магазин.")
            break
        except ValueError:
            clear_console()
            print(
                "Ошибка! Некорректный ввод веса!\n"
                "Введите ещё раз вес каждого бройлера через пробел."
            )


def handle_sale(pq: MaxBinaryHeap) -> None:
    """
    Handles the sale of a broiler from the shop's inventory.

    This function attempts to sell the broiler with the maximum weight from the
    priority queue. It prints the weight of the sold broiler and removes it
    from the queue. If the queue is empty, it informs that the inventory is empty.

    Parameters:
    pq (MaxBinaryHeap): The priority queue representing the current inventory of broilers.

    Returns:
    None

    Side effects:
    - Modifies the provided MaxBinaryHeap object by removing the maximum element.
    - Prints messages to the console about the sale or empty inventory status.
    """
    try:
        print("Продан бройлер", pq.peek_max())
        pq.extract_max()
    except IndexError:
        print("Ассортимент пуст.")


def print_broilers(pq: MaxBinaryHeap):
    """
    Displays the current inventory of broilers in the shop.

    This function checks if the priority queue of broilers is not empty.
    If there are broilers in the inventory, it prints the current list
    of broilers.

    Parameters:
    pq (MaxBinaryHeap): The priority queue representing the current inventory of broilers.

    Returns:
    None

    Side effects:
    - Prints the current inventory of broilers to the console if not empty.
    """
    if not pq.is_empty():
        print("Текущие поставки бройлеров:")
        print(pq)
