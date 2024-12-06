# Задача "Найдёт везде":

# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).

# Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.

# Также объект класса WordsFinder должен обладать следующими методами:
# get_all_words - подготовительный метод, который возвращает словарь следующего вида:
# {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
# Где:
# 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
# ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.

# Алгоритм получения словаря такого вида в методе get_all_words:
# Создайте пустой словарь all_words.
# Переберите названия файлов и открывайте каждый из них, используя оператор with.
# Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
# Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
# Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
# В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

# find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
# count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
# В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
# Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().
# for name, words in get_all_words().items():
# Логика методов find или count

# Пример результата выполнения программы:
# Представим, что файл 'test_file.txt' содержит следующий текст:
# It's a text for task Найти везде,
# Используйте его для самопроверки.
# Успехов в решении задачи!
# text text text

# Пример выполнения программы:
# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# Вывод на консоль:
# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}

# Примечания:
# Регистром слов при поиске можно пренебречь. ('teXT' ~ 'text')
# Решайте задачу последовательно - написав один метод, проверьте результаты его работы.

import string


class WordsFinder:
    def __init__(self, *args):
        self.file_names = []
        self.args = args
        self.file_names.append(args)

    def get_all_words(self):
        all_words = {}
        for files in self.file_names:
            for file in files:
                with open(file, "r", encoding="utf-8") as file:
                    lines = [line for line in file]
                    joined_lines = "".join(lines)
                    joined_lines = joined_lines.translate(
                        str.maketrans("", "", string.punctuation)
                    )
                    joined_lines = joined_lines.lower()
                    joined_lines = joined_lines.split()
                    all_words[file.name] = joined_lines
        return all_words

    def find(self, word):
        word = word.lower()
        items = self.get_all_words().items()
        dict_ = {name: words.index(word) + 1 for name, words in items}
        # for name, words in items:
        # dict_[name] = words.index(word) + 1
        return dict_

    def count(self, word):
        word = word.lower()
        items = self.get_all_words().items()
        dict_ = {name: words.count(word) for name, words in items}
        # for name, words in items:
        # dict_[name] = words.count(word)
        return dict_


finder1 = WordsFinder(
    "Walt Whitman - O Captain! My Captain!.txt",
    "Rudyard Kipling - If.txt",
    "Mother Goose - Monday’s Child.txt",
)
print(finder1.get_all_words())
# print(finder1.get_all_words().items())
print(finder1.find("the"))
print(finder1.count("the"))

finder2 = WordsFinder("test_file.txt")
print(finder2.get_all_words())  # Все слова
# print(finder1.get_all_words().items())
print(finder2.find("TEXT"))  # 3 слово по счёту
print(finder2.count("teXT"))  # 4 слова teXT в тексте всего