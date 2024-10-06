print("......Dicts......")
my_dict = {"Moscow": 1935, "Leningrad": 1955}
print(my_dict)
print("date:", my_dict["Moscow"])
# my_dict["Novosibirsk"] = 1986
print(my_dict.get("Novosibirsk"))
my_dict.update({"Kazan": 2005, "Samara": 1987})
# del my_dict["Kazan"]
# my_dict.pop("Kazan")
pc = my_dict.pop("Kazan")
print("Popped date:", pc)
print(my_dict)

###sets###
print("......SETS......")
my_set = {
    8,
    True,
    15,
    16,
    23,
    42,
    "finish",
    8,
    True,
    15,
    16,
    23,
    42,
    "finish",
}
print(my_set)
my_set.update({(7, "start")})
my_set.remove(True)
print(my_set)
