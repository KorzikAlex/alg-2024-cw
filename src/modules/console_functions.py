"""
This file contains functions to work with console in meat's shop.
"""

from os import name as os_name
from os import system

from modules.priority_queue import MaxPriorityQueue


def get_answer() -> int:
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
    weights = list(map(float, input().replace(",", ".").split()))
    for i in weights:
        pq.insert(i)
    return pq


def clear_console():
    """Очищает консоль."""
    system("cls" if os_name == "nt" else "clear")


def handle_delivery(pq: MaxPriorityQueue):
    """Обрабатывает поставку бройлеров."""
    print(
        "Сделать поставку бройлеров в магазин.\n"
        "Введите через пробел вес бройлеров:"
    )
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


def handle_sale(pq: MaxPriorityQueue):
    """Обрабатывает продажу бройлера."""
    try:
        print("Продан бройлер", pq.peek_max())
        pq.extract_max()
    except IndexError:
        print("Ассортимент пуст.")

def print_broilers(pq: MaxPriorityQueue):
    """Отображает текущие поставки бройлеров."""
    print("Текущие поставки бройлеров:")
    print(pq)