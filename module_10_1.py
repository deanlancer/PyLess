# Задача "Потоковая запись в файлы":

# Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".


# После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:
# 10, example1.txt
# 30, example2.txt
# 200, example3.txt
# 100, example4.txt

# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
# 10, example5.txt
# 30, example6.txt
# 200, example7.txt
# 100, example8.txt

# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию.

# Пример результата выполнения программы:
# Алгоритм работы кода:
# # Импорты необходимых модулей и функций
# # Объявление функции write_words
# # Взятие текущего времени
# # Запуск функций с аргументами из задачи
# # Взятие текущего времени
# # Вывод разницы начала и конца работы функций
# # Взятие текущего времени
# # Создание и запуск потоков с аргументами из задачи
# # Взятие текущего времени
# # Вывод разницы начала и конца работы потоков

# Вывод на консоль:
# Завершилась запись в файл example1.txt
# Завершилась запись в файл example2.txt
# Завершилась запись в файл example3.txt
# Завершилась запись в файл example4.txt
# Работа потоков 0:00:34.003411 # Может быть другое время
# Завершилась запись в файл example5.txt
# Завершилась запись в файл example6.txt
# Завершилась запись в файл example8.txt
# Завершилась запись в файл example7.txt
# Работа потоков 0:00:20.071575 # Может быть другое время

# Примечания:
# Не переживайте, если программа выполняется долго, учитывая кол-во слов, максимальное время выполнения в потоках не должно превышать ~20 секунд, а в функциях ~34 секунды.
# Cледует заметить, что запись в example8.txt завершилась раньше, чем в example7.txt, т.к. потоки работали почти одновременно.

import threading
import time


def write_words(word_count, file_name):
    with open(f"{file_name}", mode="w", encoding="utf-8") as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")
    return


start = time.time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end = time.time()
print((f"Работа потоков {round(end - start, 4)} сек."))

# threading
start = time.time()
thread_1 = threading.Thread(target=write_words, args=(10, "example5.txt"))
thread_1.start()
thread_2 = threading.Thread(target=write_words, args=(30, "example6.txt"))
thread_2.start()
thread_3 = threading.Thread(target=write_words, args=(200, "example7.txt"))
thread_3.start()
thread_4 = threading.Thread(target=write_words, args=(100, "example8.txt"))
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
end = time.time()
print((f"Работа потоков {round(end - start, 4)} сек."))
