import math


def unique_elements(item: list[int]) -> list[int]:
    """ Написать функцию, которая принимает на вход список
    целых чисел и возвращает новый список, содержащий только
    уникальные элементы из исходного списка. """
    set_item = set(item)
    return list(set_item)


def prime_number(number: int) -> bool:
    """ Написать функцию, которая принимает на вход два целых числа
    (минимум и максимум) и возвращает список всех простых чисел
    в заданном диапазоне. """
    if number <= 1:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


def prime_numbers_list(min_number: int, max_number: int) -> list[int]:
    result = [i for i in range(min_number, max_number + 1) if prime_number(i)]
    return result


class Point:
    """ Создать класс Point, который представляет собой точку в
    двумерном пространстве. Класс должен иметь методы для
    инициализации координат точки, вычисления расстояния до
    другой точки, а также для получения и изменения координат. """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


def sorted_list(item: list[str]) -> str:
    """ Написать программу, которая сортирует список строк
    по длине, сначала по возрастанию, а затем по убыванию. """
    result_sorted = sorted(item, key=lambda x: len(x))
    result_sorted_reverse = sorted(item, key=lambda x: len(x), reverse=True)
    return (f'{result_sorted}\n'
            f'{result_sorted_reverse}')
