"""
This file contains functions to work with console in meat's shop.
"""

from modules.priority_queue import MaxPriorityQueue


def get_answer() -> int:
    """
    This function retrieves a user's choice from a console menu.

    Parameters:
    None

    Returns:
    int: The user's choice as an integer. The value must be between 1 and 4 inclusive.
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
        raise ValueError
    return ans


def deliver_broilers(pq: MaxPriorityQueue) -> MaxPriorityQueue:
    """
    This function simulates the delivery of broilers to the meat shop.
    It takes a priority queue (MaxPriorityQueue) as input,
    where each element represents the weight of a broiler.
    The function clears the console, prints a message asking for broiler weights,
    retrieves the weights from the user, and inserts them into the priority queue.
    Finally, it prints a success message.

    Parameters:
    pq (MaxPriorityQueue): A priority queue where each element represents the weight of a broiler.

    Returns:
    MaxPriorityQueue: The same priority queue after inserting the new broiler weights.
    """
    weights = list(map(float, input().replace(",", ".").split()))
    for i in weights:
        pq.insert(i)
    print("Бройлеры успешно добавлены в магазин.")
    return pq
