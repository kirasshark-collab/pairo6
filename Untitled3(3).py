from datetime import date
year = int(input("Введіть рік події: "))
month = int(input("Введіть місяць події: "))
day = int(input("Введіть день події: "))
event = date(year, month, day)
today = date.today()
if event > today:
    print("До події залишилося:", (event - today).days, "днів")
elif event < today:
    print("Минуло днів після події:", (today - event).days)
else:
    print("Подія відбувається сьогодні")
    