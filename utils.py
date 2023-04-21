import requests
import random
from basic_word import BasicWord


def load_random_word():
    """
    Загружает список словарей с исходными словами и образованными от них словами
    с внешнего ресурса в формате JSON. Через метод .json() преобразует их в объект Python.
    Перемешивает элементы списка для выбора случайного слова.
    Возвращает экземпляр класса BasicWord с полями:
    - original_word - исходное слово;
    - set_subwords - набор подслов исходного слова.
    """
    response_json = requests.get('https://www.jsonkeeper.com/b/FZ85')
    response = response_json.json()

    random.shuffle(response)

    original_word = response[0]['word']
    set_subwords = response[0]['subwords']
    basic_word = BasicWord(original_word, set_subwords)

    return basic_word
