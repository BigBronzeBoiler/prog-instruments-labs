import checksum
import util
from vars import csv_path


def main():
    found_rows = util.find_wrong_rows(csv_path)
    checksum.serialize_result(28, checksum.calculate_checksum(found_rows))


if __name__ == "__main__":
    main()
