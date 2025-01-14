"""Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию)."""

import inspect
from module_5 import class_d as c


def introspection_info(obj):
    type_ = type(obj).__name__
    method = [a for a in dir(obj) if callable(getattr(obj, a))]
    attr_ = [a for a in dir(obj) if not a in method]
    mod = inspect.getmodule(obj)
    return {"type": type_, "method": method, "module": mod, "attributes": attr_}


result = introspection_info(c.House)
print(result)

result_2 = introspection_info(42)
print(result_2)
