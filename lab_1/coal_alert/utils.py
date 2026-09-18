import json
import random
import string
from typing import cast


def generate_random_string(length: int) -> str:
    """
    Генерация случайной строки заданной длины.
    Принимает:
        length - длину строки
    Возвращает:
        Строку длиной length
    """
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Длина строки должна быть натуральным числом")
    try:
        chars = string.ascii_letters + string.digits
        return "".join(random.choices(chars, k=length))
    except Exception as e:
        print(f"Внутренняя ошибка при генерации строки: {e}")
        raise


def read_json_file(filepath: str) -> dict[str, object]:
    """
    Чтение .json файла по указанному пути в словарь.
    """
    try:
        with open(filepath, encoding="utf-8") as fp:
            json_data = json.load(fp)

        if not isinstance(json_data, dict):
            raise ValueError("Корневой элемент JSON должен быть объектом")

        return cast(dict[str, object], json_data)
    except Exception as e:
        print(f"Не удалось открыть файл {filepath}: {e}")
        raise
