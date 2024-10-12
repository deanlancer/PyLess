my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
fint = len(my_list)
bint = 0
# wint = my_list[bint]
while bint < fint:
    wint = my_list[bint]
    bint = bint + 1
    if wint == 0:
        continue
    elif wint < 0:
        break
    print(wint)

