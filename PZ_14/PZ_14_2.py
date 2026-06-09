# Даны два целых числа A и B (A < B).
# Найти сумму квадратов всех целых чисел от A до B включительно.

import tkinter as tk
from tkinter import messagebox


def calculate_sum_of_squares():
    try:
        val_a = entry_a.get().strip()
        val_b = entry_b.get().strip()

        if not val_a or not val_b:
            messagebox.showerror("Ошибка", "Поля ввода не могут быть пустыми!")
            return

        a = int(val_a)
        b = int(val_b)

        if a >= b:
            messagebox.showerror(
                "Ошибка", "Нарушено условие задачи! Число A должно быть меньше B."
            )
            return

        total_sum = 0
        for num in range(a, b + 1):
            total_sum += num**2

        label_result.config(text=f"Результат: {total_sum}")

    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Пожалуйста, введите корректные целые числа!"
        )


root = tk.Tk()
root.title("PZ_14 - Задание 2")
root.geometry("400x250")

label_instruction = tk.Label(
    root,
    text="Найти сумму квадратов всех целых чисел\nот A до B включительно (при условии A < B).",
    font=("Arial", 10),
)
label_instruction.pack(pady=10)

label_a = tk.Label(root, text="Введите число A:")
label_a.pack()
entry_a = tk.Entry(root, width=15, justify="center")
entry_a.pack(pady=2)

label_b = tk.Label(root, text="Введите число B:")
label_b.pack()
entry_b = tk.Entry(root, width=15, justify="center")
entry_b.pack(pady=2)

button_calc = tk.Button(
    root, text="Рассчитать", command=calculate_sum_of_squares
)
button_calc.pack(pady=15)

label_result = tk.Label(root, text="Результат: ", font=("Arial", 11, "bold"))
label_result.pack(pady=5)

root.mainloop()