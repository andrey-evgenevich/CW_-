from settings import OPERATIONS_PATH
from utils import load_operations, sorted_operations, execuded_operation, five


def main():
    operations_list = load_operations(OPERATIONS_PATH)
    sort_operations = sorted_operations(operations_list)
    sorted_executed_operations = execuded_operation(sort_operations)
    five_operations = five(sorted_executed_operations)
    return five_operations


if __name__ == "__main__":
    print(main())
