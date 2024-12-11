"""
The main file.
"""

import os
from os import system
from modules.priority_queue import MaxPriorityQueue


if __name__ == "__main__":
    pq = MaxPriorityQueue()
    system("cls" if os.name == "nt" else "clear")
    print("Здравствуйте, милорд! Чтобы вы хотели сделать?\nВведите номер опции:")
    while True:
        try:
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
            break
        except ValueError:
            system("cls" if os.name == "nt" else "clear")
            print(
                "Неправильный ввод. Пожалуйста, введите число от 1 до 4.\n"
                "Введите номер опции:\n"
            )
            continue
    if ans == 1:
        pass
    if ans == 2:
        pass
    if ans == 3:
        pass
    if ans == 4:
        exit(0)
