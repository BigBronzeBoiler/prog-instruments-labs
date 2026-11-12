import csv

from vars import PATTERNS


def find_wrong_rows(filepath: str) -> list[str]:
    """
    Возвращает номера строк CSV файла, не прошедших валидацию.

    Принимает:
    - filepath - путь до csv файла с данными

    Возвращает:
    - список целочисленных номеров строк csv-файла, на которых были найдены ошибки валидации
    """
    invalid_rows = []

    with open(filepath, encoding="utf-16", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row_number, row in enumerate(reader):
            for column, pattern in PATTERNS.items():
                if not pattern.fullmatch(row[column]):
                    invalid_rows.append(row_number)
                    break

    return invalid_rows
