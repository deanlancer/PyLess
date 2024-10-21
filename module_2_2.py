first = input("Type first number:")
second = input("Type second number: ")
third = input("Type third number:")
# numbers = len({first, second, third})
if first == second == third:
    # if numbers == 1 :
    print("3")
elif first == second or second == third or first == third:
    # elif numbers == 2:
    print("2")
else:
    print("0")
