# Задача "Счётчик вызовов":

# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.

# Давайте реализуем данную фишку самостоятельно!

# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

# Пункты задачи:
# Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).

# Пример результата выполнения программы:

# Пример выполняемого кода:
# print(string_info('Capybara'))
# print(string_info('Armageddon'))
# print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
# print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
# print(calls)

# Вывод на консоль:
# (8, 'CAPYBARA', 'capybara')
# (10, 'ARMAGEDDON', 'armageddon')
# True
# False
# 4

# Примечания:
# Для использования глобальной переменной внутри функции используйте оператор global.
# Для функции is_contains лучше привести и искомую строку и все строки в списке в один регистр.V

calls = 0

def count_calls():
    global calls 
    calls += 1 

def string_info(string):
    tuple = (len(string), string.upper(), string.lower())
    count_calls()
    return tuple 

def is_contains(string, list_to_search):
    string = string.lower() 
    list_lower = [i.lower() for i in list_to_search]
    # for i in list_to_search:
        # i = i.lower()
        # list_lower.append(i)
    count_calls()
    if string in list_lower :
       return True 
    else:
       return False

# string_info("Capybara")
# is_contains("Peks", ["Rex", "peks", "feks"])
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

# list_to_search = ["Rex", "PEks", "FeKs"]
# list_lower = []
# for i in list_to_search:
        # # print(i)
        # i = i.lower()
        # list_lower.append(i)
# print(list_lower)

# list_to_search = ["Rex", "PEks", "FeKs"]
# list_lower = [i.lower() for i in list_to_search]
# print(list_lower)
