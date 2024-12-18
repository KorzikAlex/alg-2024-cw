"""
This file contains tests for max binary heap.
"""

import pytest
from modules.max_binary_heap import MaxBinaryHeap


# Фикстура для создания экземпляра MaxBinaryHeap
@pytest.fixture
def max_heap():
    return MaxBinaryHeap()


# Тест на проверку инициализации пустой кучи
def test_initial_heap_is_empty(max_heap):
    assert max_heap.is_empty()
    assert len(max_heap) == 0


# Тест на вставку элементов и проверку максимального элемента
def test_insert_and_peek_max(max_heap):
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(15)
    assert max_heap.peek_max() == 20


# Тест на извлечение максимального элемента
def test_extract_max(max_heap):
    max_heap.insert(10)
    max_heap.insert(30)
    max_heap.insert(20)
    assert max_heap.extract_max() == 30
    assert max_heap.extract_max() == 20
    assert max_heap.extract_max() == 10
    assert max_heap.is_empty()


# Тест на извлечение из пустой кучи
def test_extract_max_from_empty_heap(max_heap):
    with pytest.raises(IndexError):
        max_heap.extract_max()


# Тест на проверку пустоты кучи
def test_is_empty(max_heap):
    assert max_heap.is_empty()
    max_heap.insert(10)
    assert not max_heap.is_empty()


# Тест на проверку длины кучи
def test_len(max_heap):
    assert len(max_heap) == 0
    max_heap.insert(10)
    assert len(max_heap) == 1
    max_heap.insert(20)
    assert len(max_heap) == 2
    max_heap.extract_max()
    assert len(max_heap) == 1


# Тест на вставку и извлечение большого количества элементов
def test_large_number_of_elements(max_heap):
    elements = [i for i in range(100, 0, -1)]  # [100, 99, ..., 1]
    for element in elements:
        max_heap.insert(element)
    assert len(max_heap) == 100
    for i in range(100, 0, -1):
        assert max_heap.extract_max() == i
    assert max_heap.is_empty()


# Тест на вставку одинаковых элементов
def test_insert_duplicate_elements(max_heap):
    max_heap.insert(5)
    max_heap.insert(5)
    max_heap.insert(5)
    assert max_heap.extract_max() == 5
    assert max_heap.extract_max() == 5
    assert max_heap.extract_max() == 5
    assert max_heap.is_empty()


# Тест на вставку и извлечение элементов в случайном порядке
def test_random_order_insertion_and_extraction(max_heap):
    elements = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    for element in elements:
        max_heap.insert(element)
    sorted_elements = sorted(elements, reverse=True)
    for element in sorted_elements:
        assert max_heap.extract_max() == element
    assert max_heap.is_empty()


# Тест на строковое представление кучи
def test_str_representation(max_heap):
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(15)
    assert str(max_heap) == "20, 10, 15"


if __name__ == "__main__":
    pytest.main()
