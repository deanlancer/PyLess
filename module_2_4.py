# Задача "Всё не так уж просто":
# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).
# Пункты задачи:
# Создайте пустые списки primes и not_primes.
# При помощи цикла for переберите список numbers.
# Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
# Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
# В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
# Выведите списки primes и not_primes на экран(в консоль).
# Пример результата выполнения программы:
# Исходный код:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Вывод на консоль:
# Primes: [2, 3, 5, 7, 11, 13]
# Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
# Примечания:
# Учтите, что число 1 не является ни простым, ни составным числом, поэтому оно отсутствует в конечных списках.
# Для проверки на простоту числа вам нужно убедиться, что выбранное число не делиться ни на что в диапазоне от 2 до этого числа(не включительно).
# Попробуйте оптимизировать(ускорить) процесс выяснения простоты числа при помощи оператора break, когда найдёте делитель. (Не обязательно)
# Переменные меняющее своё булевое состояние на противоположное в процессе проверки, как is_prime, в кругах разработчиков называются перменными-флагами(flag).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
# is_prime = True

# for i in numbers[1:]:
    # for j in numbers[1:i]:
      # print(f"{i} * {j} = {i * j}")

# for i in numbers[1:]:
    # is_prime = True
    # for j in numbers[1:i]: # such way doesn't work with this loop (NB)
        # if i & j == 0:
            # is_prime = False
            # break
    # if is_prime:
        # primes.append(i) 
    # else:
        # not_primes.append(i) 

# for i in range(2,16): # needed to include 15
     # is_prime = True  
     # for j in range(2, i):  # using range
         # if i % j == 0:
             # is_prime = False
             # break
     # if is_prime:
         # primes.append(i)
     # else:
         # not_primes.append(i)

for i in numbers[1:]:
    is_prime = True  
    for j in range(2, i):
        if i % j == 0:
           is_prime = False
           break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print("Primes:", primes)
print("Not Primes:", not_primes)


