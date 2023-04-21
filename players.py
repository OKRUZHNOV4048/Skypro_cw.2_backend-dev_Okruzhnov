class Player:

    def __init__(self, user_name="", user_words_used=None):
        if user_words_used is None:
            user_words_used = []
        self.user_name = user_name
        self.user_words_used = user_words_used

    def __repr__(self):
        return f"Игрок и использованные им слова ('{self.user_name}', {self.user_words_used})"

    def get_number_words_used(self):
        """
        Подсчитывает количество использованных слов и возвращает int.
        """
        return len(self.user_words_used)

    def add_user_word(self, entered_word):
        """
        Добавляет введенное слово в список использованных слов.
        """
        self.user_words_used.append(entered_word)
        return self.user_words_used

    def check_reentry_word(self, entered_word):
        """
        Проверяет факт использования введенного слова на предыдущих пользовательских вводах и возвращает bool.
        """
        if entered_word not in self.user_words_used:
            return True
