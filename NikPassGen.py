import random
import string


def generate_passwords(nickname, count=1000000000, block_size=1000000, file_name="passwords.txt"):
    characters = string.ascii_letters + string.digits + string.punctuation

    # Открываем файл на запись в режиме добавления
    with open(file_name, "a") as file:
        for i in range(count):
            # Случайная мутация никнейма (изменение регистра букв)
            mutated_nickname = ''.join(random.choice([char.lower(), char.upper()]) for char in nickname)

            # Добавление случайных символов в начало и конец
            prefix = ''.join(random.choices(characters, k=random.randint(1, 3)))
            suffix = ''.join(random.choices(characters, k=random.randint(1, 3)))

            # Генерация пароля с ником в середине
            password = prefix + mutated_nickname + suffix

            # Выводим пароль в консоль
            print(password)

            # Записываем пароль в файл
            file.write(password + "\n")

            # Опционально: выводим информацию о прогрессе каждые block_size паролей
            if (i + 1) % block_size == 0:
                print(f"{i + 1} паролей сгенерировано и записано в файл...")


# Пример использования:
nickname = input("Введите никнейм: ")
generate_passwords(nickname)
