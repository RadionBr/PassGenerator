import random
import string


def generate_passwords(nickname, count=1000000):
    characters = string.ascii_letters + string.digits + string.punctuation

    for _ in range(count):
        # Случайная мутация никнейма (изменение регистра букв)
        mutated_nickname = ''.join(random.choice([char.lower(), char.upper()]) for char in nickname)

        # Добавление случайных символов в начало и конец
        prefix = ''.join(random.choices(characters, k=random.randint(1, 3)))
        suffix = ''.join(random.choices(characters, k=random.randint(1, 3)))

        # Генерация пароля с ником в середине
        password = prefix + mutated_nickname + suffix

        # Выводим пароль сразу
        print(password)


# Пример использования:
nickname = input("Введите никнейм: ")
generate_passwords(nickname)
