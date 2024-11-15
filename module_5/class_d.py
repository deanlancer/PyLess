class House:
    houses_history = []

    def __new__(cls, *args):
        cls.args = args
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        # self.house_history = []

    def __del__(self):
        print(f"{self.name} снесен, но он останется в истории")

    def go_to(self, new_floor):
        if new_floor in range(self.number_of_floors):
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Such floor does not exist!")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return NotImplemented

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        return NotImplemented

    def __iadd__(self, value):
        return self.__add__(value)
        # return self + value

    def __radd__(self, value):
        return self.__add__(value)
        # return self + value
