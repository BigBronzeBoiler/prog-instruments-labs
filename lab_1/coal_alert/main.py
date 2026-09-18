import argparse
import subprocess

import collisions
import gui
import utils


def parse_args() -> argparse.Namespace:
    """
    Парсинг аргументов командной строки:
    -Выбор 1-го из 2-ух режимов работы программы на выбор
    -Путь до .json файла с настройками
    """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--cli", action="store_true", help="Запуск в режиме командной строки вместо GUI"
    )
    group.add_argument(
        "--gui", action="store_true", help="Запуск в режиме GUI вместо командной строки"
    )
    group.add_argument("--uni", action="store_true", help="Запуск юнит-тестов")

    parser.add_argument("-jp", "--json-path", help="Путь до .json файла с настройками.")

    return parser.parse_args()


def main():
    try:
        args = parse_args()

        if args.cli:
            mode = "cli"
        elif args.gui:
            mode = "gui"
        elif args.uni:
            mode = "uni"

        match mode:
            case "gui":
                gui.run_gui()
            case "cli":
                if not isinstance(args.json_path, str):
                    raise ValueError("Для режима CLI необходимо указать --json-path")

                settings = utils.read_json_file(args.json_path)

                raw_bits = settings.get("bits")
                experiments = settings.get("experiments")
                str_length = settings.get("str_length")

                if not isinstance(raw_bits, list) or not all(
                    isinstance(bit, int) for bit in raw_bits
                ):
                    raise ValueError("Параметр bits должен быть списком целых чисел")

                if not isinstance(experiments, int):
                    raise ValueError("Параметр experiments должен быть целым числом")

                if not isinstance(str_length, int):
                    raise ValueError("Параметр str_length должен быть целым числом")

                bits = [bit for bit in raw_bits if isinstance(bit, int)]

                collisions.run_experiments(bits, experiments, str_length)
            case "uni":
                subprocess.run("python collision_unittests.py")

    except Exception as e:
        print("Критическая ошибка приложения:", e)


if __name__ == "__main__":
    main()
