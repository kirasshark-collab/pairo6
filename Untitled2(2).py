import random
import statistics
n = int(input("Введіть кількість оцінок: "))
if n <= 0:
    print("Кількість оцінок має бути додатною.")
else:
    grades = []
    for i in range(n):
        grades.append(random.randint(1, 12))
    minimum = min(grades)
    maximum = max(grades)
    average = statistics.mean(grades)
    median = statistics.median(grades)
    count = 0
    for grade in grades:
        if grade >= 10:
            count += 1
    print("Оцінки:", grades)
    print("Мінімальна оцінка:", minimum)
    print("Максимальна оцінка:", maximum)
    print("Середнє арифметичне:", round(average, 2))
    print("Медіана:", median)
    