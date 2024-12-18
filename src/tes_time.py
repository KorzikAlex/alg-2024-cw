import timeit
import random

from modules.max_binary_heap import MaxBinaryHeap
# Создаем макс-кучу
def create_max_heap(size):
    heap = MaxBinaryHeap([random.randint(1, 1000000) for _ in range(size)])
    return heap

# Измерение времени показа максимального элемента
def measure_peek_max(heap):
    start_time = timeit.default_timer()
    heap.peek_max()  # Показываем максимальный элемент
    end_time = timeit.default_timer()
    return end_time - start_time

# Размеры выборки
sizes = [100, 1000, 10000, 100000, 1000000]

# Измерение времени для каждого размера выборки
for size in sizes:
    heap = create_max_heap(size)
    
    # Измерение времени показа максимального элемента
    peek_time = measure_peek_max(heap)
    print(f"Размер выборки: {size}, Время показа максимума: {peek_time:.6f} сек")