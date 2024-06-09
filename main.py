from settings import OPERATIONS_PATH
from utils import load_operations, sorted_operations, executed_operation, five


def main():
    operations_list = load_operations(OPERATIONS_PATH)
    sort_operations = sorted_operations(operations_list)
    sorted_executed_operations = executed_operation(sort_operations)
    five_operations = five(sorted_executed_operations)
    print(five_operations)
    for correct in five_operations:
        date = correct["date"]
        description = correct["description"]
        op_from = correct["from"]
        op_to = correct["to"]
        operation_amount = correct["operationAmount"]
        currency = correct['currency']
        print(f'{date} {description}\n'
              f'{op_from[0: -12]} {op_from[-12: -10]}** **** {op_from[-5: -1]} -> Счет **{op_to[-5: -1]}\n'
              f'{operation_amount} {currency}\n')


if __name__ == "__main__":
    print(main())
