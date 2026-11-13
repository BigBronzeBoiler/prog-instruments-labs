import argparse

import asym
import keygen
import sym
import util


def parse_args():
    """
    Парсинг аргументов командной строки:
    -Выбор 1-го из 3-ёх режимов работы программы на выбор
    -Путь до .json файла с настройками
    """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-gen", "--generation", help="Запускает режим генерации ключей")
    group.add_argument("-enc", "--encryption", help="Запускает режим шифрования")
    group.add_argument("-dec", "--decryption", help="Запускает режим дешифрования")

    group2 = parser.add_mutually_exclusive_group(required=True)
    group2.add_argument("-cam", "--camellia", help="Использование алгоритма Camellia")
    group2.add_argument("-aes", "--aes", help="Использование алгоритма AES")

    parser.add_argument("-jp", "--json_path", help="Путь до .json файла с настройками.")

    return parser.parse_args()


def main():
    try:
        args = parse_args()
        json_settings = util.read_json_file(args.json_path)

        init_file_path = json_settings.get("initial_file")
        ciph_file_path = json_settings.get("cipher_text")
        dec_file_path = json_settings.get("decrypted_file")
        sym_key_path = json_settings.get("symmetric_key")
        pub_key_path = json_settings.get("public_key")
        sec_key_path = json_settings.get("secret_key")
        key_length = int(json_settings.get("key_length"))

        if args.generation:
            sym_key = keygen.volshebniy_kluch(key_length)
            keygen.asym_keygen(pub_key_path, sec_key_path)
            encrypted_key = asym.encrypt_with_public_key(sym_key, pub_key_path)
            util.write_file(sym_key_path, encrypted_key)
            return

        encrypted_key = util.read_file(sym_key_path)
        sym_key = asym.decrypt_with_private_key(encrypted_key, sec_key_path)

        if args.camellia:
            encrypt = sym.encrypt_data_camellia
            decrypt = sym.decrypt_data_camellia
        elif args.aes:
            encrypt = sym.encrypt_data_aes
            decrypt = sym.decrypt_data_aes

        if args.encryption:
            ciphertext = encrypt(init_file_path, sym_key)
            util.write_file(ciph_file_path, ciphertext)
        else:
            plaintext = decrypt(ciph_file_path, sym_key)
            util.write_file(dec_file_path, plaintext)

    except Exception as e:
        print(f"В ходе работы произошла ошибка {e}")


if __name__ == "__main__":
    main()
