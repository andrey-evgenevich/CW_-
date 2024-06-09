from utils import five


def test_five_integer():
    """
    Тест числа
    """
    assert five([5, 6, 2, 6, 10, 9, 100500]) == [5, 6, 2, 6, 10]


def test_five_strings():
    """
    Тест строки
    """
    assert five(['f', 'a', 'y', 'n', 'u', 'h', 'u']) == ['f', 'a', 'y', 'n', 'u']


def test_five_float():
    """
    Тест числа с плавающей точкой
    """
    assert five([2.15, 53.56, 43.0, 9867.876543, 657.7845, 5.7]) == [2.15, 53.56, 43.0, 9867.876543, 657.7845]


def test_five_all():
    """
    Тест всe типы
    """
    assert five([2.56, 'python', 6, [1, 2, 3, 4, 5], {'letters': 'words'}, 'h', 12355]) == [2.56, 'python', 6, [1, 2, 3, 4, 5], {'letters': 'words'}]


def test_five_empty():
    """
    Тест пусто
    """
    assert five([]) == []
