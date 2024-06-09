import pytest
from utils import sorted_operations


def test_sorted_operations_empty():
    """
    Тест пустого списка
    """
    assert sorted_operations([]) == []


def test_sorted_operations_int():
    """
    Тест списка чисел
    """
    assert sorted_operations([1, 2, 3, 4, 5, 6, 7]) == []


def test_sorted_operations_str():
    """
    Тест списка строк
    """
    assert sorted_operations(['h', 'fg,', 'w', 'd', 'g', 'l']) == []


def test_sorted_operations_date():
    """
    Тест списка дат
    """
    assert sorted_operations([{"date": "2019-03-23T01:09:46.296404"},
                              {"date": "2019-04-04T23:20:05.206878"}, {"date": "2018-03-23T10:45:06.972075"}]) == [
               {'date': '2019-04-04T23:20:05.206878'}, {'date': '2019-03-23T01:09:46.296404'},
               {'date': '2018-03-23T10:45:06.972075'}]
