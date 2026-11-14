import math
radius = float(input("Введіть радіус кола: "))
a = float(input("Введіть перший катет: "))
b = float(input("Введіть другий катет: "))
items = int(input("Введіть кількість предметів: "))
capacity = int(input("Введіть кількість предметів в одній упаковці: "))
area = math.pi * radius ** 2
hypotenuse = math.sqrt(a ** 2 + b ** 2)
packages = math.ceil(items / capacity)
print("Площа кола:", round(area, 2))
print("Гіпотенуза:", round(hypotenuse, 2))
print("Необхідна кількість упаковок:", packages)


