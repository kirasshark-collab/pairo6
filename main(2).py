import tkinter as tk
from tkinter import messagebox
import student_utils
students = ["Anna", "Ivan", "Olha"]
def make_report(count):
    report = ""
    for student in students:
        grades = student_utils.generate_grades(count)
        average = student_utils.average_grade(grades)
        level = student_utils.get_level(average)
        report += f"{student}: {grades} - {average} - {level}\n"
    return report
def show_report():
    value = entry.get().strip()
    if not value.isdecimal():
        messagebox.showerror("Помилка", "Введіть ціле число від 1 до 20")
        return
    count = int(value)
    if count < 1 or count > 20:
        messagebox.showerror("Помилка", "Кількість оцінок має бути від 1 до 20")
        return
    report = make_report(count)
    print(report)
    result.delete("1.0", tk.END)
    result.insert(tk.END, report)
window = tk.Tk()
window.title("Статистика учнів")
label = tk.Label(window, text="Введіть кількість оцінок для кожного учня (1–20):")
label.pack()
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="Сформувати звіт", command=show_report)
button.pack()
result = tk.Text(window, height=10, width=55)
result.pack()
window.mainloop()
