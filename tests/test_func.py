import pytest
import math
from task import unique_elements, prime_numbers_list, Point


@pytest.mark.parametrize("item, expected_result", [([1, 2, 3, 1, 2, 4], [1, 2, 3, 4]),
                                                   ([5, 5, 5, 5, 5], [5]),
                                                   ([], [])
                                                   ])
def test_unique_elements(item, expected_result):
    assert unique_elements(item) == expected_result


@pytest.mark.parametrize("min_number, max_number, expected_result", [(2, 10, [2, 3, 5, 7]),
                                                                     (11, 20, [11, 13, 17, 19]),
                                                                     (1, 5, [2, 3, 5]),
                                                                     (20, 30, [23, 29])
                                                                     ])
def test_prime_numbers_list(min_number, max_number, expected_result):
    assert prime_numbers_list(min_number, max_number) == expected_result


def test_point_distance():
    point1 = Point(0, 0)
    point2 = Point(3, 4)
    distance = point1.distance(point2)
    assert distance == 5


def test_point_coordinates():
    point = Point(2, 3)
    x, y = point.get_coordinates()
    assert x == 2
    assert y == 3


def test_point_set_coordinates():
    point = Point(0, 0)
    point.set_coordinates(4, 5)
    x, y = point.get_coordinates()
    assert x == 4
    assert y == 5


if __name__ == '__main__':
    pytest.main()
