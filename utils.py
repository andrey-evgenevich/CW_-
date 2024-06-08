from json import load
from settings import OPERATIONS_PATH


def load_operations(path):
    """Преобразует файл из json в читаемый формат"""
    with open(path, encoding="utf-8") as file:
        return load(file)


print(load_operations(OPERATIONS_PATH))
