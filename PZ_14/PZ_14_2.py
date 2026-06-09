import tkinter as tk
from tkinter import messagebox


class BMICalculator(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Калькулятор ИМТ")
        self.geometry("380x320")
        self.resizable(False, False)
        self.configure(bg="#f5f5f5")

        self.create_widgets()

    def create_widgets(self):
        """Создание элементов интерфейса калькулятора"""
        # Главный контейнер
        main_frame = tk.Frame(self, bg="#f5f5f5", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Заголовок приложения
        title = tk.Label(
            main_frame,
            text="Расчет Индекса Массы Тела",
            font=("Arial", 14, "bold"),
            bg="#f5f5f5",
            fg="#2c3e50",
        )
        title.pack(pady=(0, 15))

        # Поле ввода Веса
        lbl_weight = tk.Label(
            main_frame,
            text="Вес (в килограммах):",
            font=("Arial", 10),
            bg="#f5f5f5",
        )
        lbl_weight.pack(anchor="w")
        self.entry_weight = tk.Entry(main_frame, font=("Arial", 11), bd=2)
        self.entry_weight.pack(fill=tk.X, pady=(2, 10))

        # Поле ввода Роста
        lbl_height = tk.Label(
            main_frame,
            text="Рост (в сантиметрах):",
            font=("Arial", 10),
            bg="#f5f5f5",
        )
        lbl_height.pack(anchor="w")
        self.entry_height = tk.Entry(main_frame, font=("Arial", 11), bd=2)
        self.entry_height.pack(fill=tk.X, pady=(2, 15))

        # Кнопка расчета
        btn_calc = tk.Button(
            main_frame,
            text="Рассчитать ИМТ",
            font=("Arial", 11, "bold"),
            bg="#2ecc71",
            fg="white",
            relief=tk.RAISED,
            command=self.calculate_bmi,
        )
        btn_calc.pack(fill=tk.X, ipady=5)

        # Зона вывода результата
        self.lbl_result = tk.Label(
            main_frame,
            text="Результат появится здесь",
            font=("Arial", 11, "italic"),
            bg="#f5f5f5",
            fg="#7f8c8d",
        )
        self.lbl_result.pack(pady=(15, 0))

    def calculate_bmi(self):
        """Логика вычисления ИМТ и валидация ошибок"""
        try:
            # Получение и обработка введенных данных
            weight = float(self.entry_weight.get().replace(",", "."))
            height_cm = float(self.entry_height.get().replace(",", "."))

            # Логическая валидация на адекватность параметров
            if weight <= 0 or height_cm <= 0:
                raise ValueError("Значения должны быть строго больше нуля.")
            if height_cm > 250 or weight > 300:
                raise ValueError("Введены нереалистичные параметры тела.")

            # Формула расчета: ИМТ = Вес (кг) / Рост (м)^2
            height_m = height_cm / 100
            bmi = weight / (height_m**2)

            # Интерпретация полученных результатов
            if bmi < 18.5:
                category = "Дефицит массы тела"
                color = "#3498db"
            elif 18.5 <= bmi < 25:
                category = "Нормальный вес"
                color = "#2ecc71"
            elif 25 <= bmi < 30:
                category = "Избыточный вес (предожирение)"
                color = "#f1c40f"
            else:
                category = "Ожирение"
                color = "#e74c3c"

            # Вывод отформатированного текста на экран
            self.lbl_result.config(
                text=f"Ваш ИМТ: {bmi:.2f}\nКатегория: {category}",
                fg=color,
                font=("Arial", 11, "bold"),
            )

        except ValueError as err:
            # Обработка пустых полей, букв вместо цифр и неверных значений
            messagebox.showerror(
                "Ошибка ввода",
                f"Пожалуйста, введите корректные числовые значения.\n"
                f"Детали: {err}",
            )


if __name__ == "__main__":
    app = BMICalculator()
    app.mainloop()