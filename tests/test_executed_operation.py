from utils import executed_operation
import pytest


def test_executed_operation_empty():
    """
    Тест пустого списка
    """
    assert executed_operation([]) == []


def test_executed_attribute_error():
    """
    Тест списка чисел
    """
    with pytest.raises(AttributeError):
        assert executed_operation([1, 2, 3, 5, 100500, 605465, 565, 5498])
        raise AttributeError("Функция принимает только определенные списки библиотек или пустые библиотеки")


def test_executed_operations_correct():
    """
    Тест корректного списка
    """
    assert executed_operation([{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                                'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                                'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                                'to': 'Счет 64686473678894779589'},
                               {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
                                'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
                                'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
                                'to': 'Счет 35383033474447895560'},
                               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                                'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                                'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                                'to': 'Счет 11776614605963066702'}]) == [
               {'date': '26.08.2019', 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                'to': 'Счет 64686473678894779589', 'operationAmount': '31957.58', 'currency': 'руб.'},
               {'date': '03.07.2019', 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
                'to': 'Счет 35383033474447895560', 'operationAmount': '8221.37', 'currency': 'USD'},
               {'date': '30.06.2018', 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                'to': 'Счет 11776614605963066702', 'operationAmount': '9824.07', 'currency': 'USD'}]
