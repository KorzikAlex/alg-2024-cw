"""
The main file.
"""

from os import name as os_name
from os import system

from modules.priority_queue import MaxPriorityQueue
from modules.console_functions import get_answer, deliver_broilers

if __name__ == "__main__":
    pq: MaxPriorityQueue = MaxPriorityQueue()
    system("cls" if os_name == "nt" else "clear")
    print("Здравствуйте, милорд! Чтобы вы хотели сделать?")
    while True:
        while True:
            try:
                print("Введите номер опции:")
                ans: int = get_answer()
                break
            except ValueError:
                system("cls" if os_name == "nt" else "clear")
                print(
                    "Ошибка! Неправильный ввод.\n"
                    "Пожалуйста, введите число от 1 до 4.\n"
                    "Введите номер опции:\n"
                )
                continue
        if ans == 1:
            while True:
                try:
                    system("cls" if os_name == "nt" else "clear")
                    print(
                        "Сделать поставку бройлеров в магазин.\n"
                        "Введите через пробел вес бройлеров:"
                    )
                    pq = deliver_broilers(pq)
                    print("Бройлеры в ассортименте:", pq)
                    break
                except ValueError:
                    system("cls" if os_name == "nt" else "clear")
                    print(
                        "Ошибка! Некорректный ввод веса!\n"
                        "Введите ещё раз вес каждого бройлера через пробел."
                    )
                    continue
        elif ans == 2:
            print("Бройлеры в ассортименте:", pq)
        elif ans == 3:
            try:
                system("cls" if os_name == "nt" else "clear")
                print("Продан бройлер", pq.peek_max())
                pq.extract_max()
                print("Бройлеры в ассортименте:", pq)
            except IndexError:
                system("cls" if os_name == "nt" else "clear")
                print("Ассортимент пуст.")
        elif ans == 4:
            exit(0)
