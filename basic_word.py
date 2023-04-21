class BasicWord:

    def __init__(self, original_word, set_subwords):
        self.original_word = original_word
        self.set_subwords = set_subwords

    def __repr__(self):
        return f"Исходное слово с набором подслов ('{self.original_word}', {self.set_subwords})"

    def check_word(self, entered_word):
        """
        Проверяет веденное слово по списку допустимых подслов возвращает bool.
        """
        if entered_word in self.set_subwords:
            return True

    def count_subwords(self):
        """
        Подсчитывает количество подслов (возвращает int).
        """
        return len(self.set_subwords)
