# Задание:

# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.

# Пример:
# result = sum_three(2, 3, 6)
# print(result)

# Результат консоли:
# Простое
# 11

# Примечания:
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three


def is_prime(func):
    def wrapper(*args):
        result_ = func(*args)
        is_prime = True
        for i in range(2, result_):
            if result_ % i == 0:
                is_prime = False
        if is_prime:
            print("Prime")
        else:
            print("Not Prime")
        return result_

    return wrapper


@is_prime
def sum_three(first: int, second: int, third: int):
    sum_ = first + second + third
    return sum_


result = sum_three(2, 3, 6)
print(result)
result = sum_three(0, 2, 2)
print(result)
