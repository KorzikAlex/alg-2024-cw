"""
The main file.
"""
from modules.max_binary_heap import MaxBinaryHeap
from modules.console_functions import get_answer, clear_console, handle_delivery, handle_sale, print_broilers


def main() -> None:
    """
    The main function of program.
    """
    pq: MaxBinaryHeap = MaxBinaryHeap()
    clear_console()
    print("Здравствуйте, милорд! Чтобы вы хотели сделать?")
    while True:
        try:
            print("Введите номер опции:")
            ans: int = get_answer()
        except ValueError:
            clear_console()
            print(
                "Ошибка! Неправильный ввод.\n"
                "Пожалуйста, введите число от 1 до 4."
            )
            continue
        if ans == 1:
            clear_console()
            handle_delivery(pq)
            print_broilers(pq)
        elif ans == 2:
            clear_console()
            print_broilers(pq)
        elif ans == 3:
            clear_console()
            handle_sale(pq)
            print_broilers(pq)
        elif ans == 4:
            exit(0)


if __name__ == "__main__":
    main()
