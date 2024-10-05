immutable_var = ("lsp", "black", "cmp", 1, 1.5, True)
print("Immutable list: ", immutable_var)
# immutable_var[0] = 45
# print(immutable_var) - 'tuple' object does not support item assignment
mutable_list = immutable_var, [13, "V"]
# mutable_list[0][0] = 11 - 'tuple' object does not support item assignment
mutable_list[1][0] = 222
print("Mutable list: ", mutable_list)
