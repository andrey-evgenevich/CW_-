from json import load
from datetime import datetime


def load_operations(path):
    """Преобразует файл из json в читаемый формат"""
    with open(path, encoding="utf-8") as file:
        operations = load(file)
        return operations


def sorted_operations(operations_list):
    """
    Сортировка операций по дате в обратном порядке
    """
    return sorted(operations_list, key=lambda x: x.get('date', ''), reverse=True)


def executed_operation(operations_list):
    """
    Создание списка обработанных операций
    """
    operations = []
    for operation in operations_list:
        if operation.get('state') == 'EXECUTED':
            date_str = operation.get('date', '')
            if date_str:
                date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
                formatted_date = date.strftime('%d.%m.%Y')
                operations.append({
                    'date': formatted_date,
                    'description': operation.get('description', ''),
                    'from': operation.get('from', ''),
                    'to': operation.get('to', ''),
                    'operationAmount': operation.get('operationAmount', {}).get('amount', ''),
                    'currency': operation.get('operationAmount', {}).get('currency', {}).get('name', '')
                })
    return operations


def five(operation):
    """Возвращает список из пяти последних операций"""
    five_last = operation[0: 5]
    return five_last
