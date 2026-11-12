import json
import hashlib
from typing import List


def calculate_checksum(row_numbers: List[int]) -> str:
    """
    Вычисляет md5 хеш от списка целочисленных значений.

    ¯\\_(ツ)_/¯
    
    Принимает:
    - row_numbers - список целочисленных номеров
    
    Возвращает:
    - md5 хеш
    """
    row_numbers.sort()
    return hashlib.md5(json.dumps(row_numbers).encode('utf-8')).hexdigest()


def serialize_result(variant: int, checksum: str) -> None:
    """
    Метод для сериализации результатов лабораторной в файл results.json

    Принимает:
        - variant - номер варианта лабораторной работы
        - checksum - контрольная сумма
    """
    data = {
            "variant": str(variant),
            "checksum": checksum
    }
    data = json.dumps(data, indent=2)
    with open("result.json", "w", encoding="utf-8") as f:
        f.write(data)


if __name__ == "__main__":
    print(calculate_checksum([1, 2, 3]))
    print(calculate_checksum([3, 2, 1]))
