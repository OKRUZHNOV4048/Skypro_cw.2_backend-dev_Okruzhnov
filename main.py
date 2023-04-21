# Skypro. Курс "Python-разработчик 2.0". Поток 19.0. Окружнов Алексей.
# Курсовая работа 2.
# Слова из слова.

from players import Player
from utils import load_random_word


def main():
    user_name = input("Введите имя игрока\n")
    # Создание экземпляра player класса Player и присваивание ему первого поля user_name.
    player = Player(user_name)
    basic_word = load_random_word()
    # С помощью метода count_subwords() определяется
    # количество слов в наборе подслов, который является атрибутом экземпляра basic_word класса BasicWord.
    # Атрибут был создан с помощью функции load_random_word(), представленной в модуле utils.py, которая вызвана
    # на 12 строке.
    number_words_set = basic_word.count_subwords()
    user_words_used = input(f"Привет, {user_name}!\n"
                            f"Составьте {number_words_set} слов из слова '{basic_word.original_word}'!\n"
                            "Слова должны быть не короче 3 букв.\n"
                            "Чтобы закончить игру, угадайте все слова или напишите 'stop' или 'стоп'\n"
                            "Поехали, ваше первое слово?\n")

    while True:
        # Далее условное ветвление, которое:
        # 1. Проверяет условие по количеству букв в веденном пользователем слове.
        if len(user_words_used) <= 2:
            user_words_used = input("Слишком короткое слово. Попробуйте еще раз!\n")
        # 2. Проверят пользовательский ввод 'stop' или 'стоп' для прерывания цикла.
        elif user_words_used == 'стоп' or user_words_used == 'stop':
            break
        # 3. Через метод check_reentry_word проверяет, вводил ли пользователь подслово на предыдущих итерациях.
        elif player.check_reentry_word(user_words_used) is not True:
            user_words_used = input("Слово уже использовалось! Ваше следующее слово?\n")
        # 4. Через метод check_word() проверяет отсутствие введенного пользователем слова в наборе подслов.
        elif basic_word.check_word(user_words_used) is not True:
            user_words_used = input("Неверно! Ваше следующее слово?\n")
        # 5. Через метод check_word() определяет есть ли введенное пользователем слово в наборе подслов.
        # В той же итерации цикла, что и проверка через check_word() выполняет проверку
        # не достигла ли длина списка пользовательских слов (второго поля экземпляра player класса Player)
        # дины набора подслов, полученного из load_random_word(), определяемого через метод count_subwords()
        # класса BasicWord.
        elif basic_word.check_word(user_words_used) is True and player.check_reentry_word(user_words_used) is True:
            player.add_user_word(user_words_used)
            if player.get_number_words_used() == number_words_set:
                break
            user_words_used = input("Верно! Ваше следующее слово?\n")

    number_guessed_words = player.get_number_words_used()
    print(f"Игра завершена, вы угадали {number_guessed_words} слов!\n"
          f"Вы угадали слова: {', '.join(player.user_words_used)}!")


main()
