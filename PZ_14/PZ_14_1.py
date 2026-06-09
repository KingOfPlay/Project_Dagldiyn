import tkinter as tk
from tkinter import messagebox, ttk


class AdminDashboard(tk.Tk):

    def __init__(self):
        super().__init__()

        # Настройка главного окна
        self.title("HTML5 Admin Template - Dashboard")
        self.geometry("1000x650")
        self.configure(bg="#f4f6f9")

        # Цветовая палитра прототипа
        self.COLOR_PRIMARY = "#2c3e50"  # Темно-синий для сайдбара
        self.COLOR_ACCENT = "#3498db"  # Голубой акцент
        self.COLOR_BG = "#f4f6f9"  # Светлый фон
        self.COLOR_CARD = "#ffffff"  # Белый для карточек

        self.create_header()
        self.create_sidebar()
        self.create_main_content()

    def create_header(self):
        """Создание верхней панели (Header)"""
        header = tk.Frame(self, bg=self.COLOR_PRIMARY, height=50)
        header.pack(side=tk.TOP, fill=tk.X)
        header.pack_propagate(False)

        # Логотип / Название панели
        logo_label = tk.Label(
            header,
            text="ADMIN PANEL",
            font=("Arial", 14, "bold"),
            fg="white",
            bg=self.COLOR_PRIMARY,
        )
        logo_label.pack(side=tk.LEFT, padx=20, pady=10)

        # Кнопка выхода / Профиль
        logout_btn = tk.Button(
            header,
            text="Выйти",
            bg=self.COLOR_ACCENT,
            fg="white",
            relief=tk.FLAT,
            command=self.logout,
        )
        logout_btn.pack(side=tk.RIGHT, padx=20, pady=12)

    def create_sidebar(self):
        """Создание бокового меню навигации (Sidebar)"""
        sidebar = tk.Frame(self, bg="#34495e", width=200)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)

        # Элементы меню
        menu_items = [
            "📊 Главная",
            "📈 Аналитика",
            "👥 Пользователи",
            "📦 Товары",
            "⚙️ Настройки",
        ]
        for item in menu_items:
            btn = tk.Button(
                sidebar,
                text=item,
                font=("Arial", 11),
                fg="white",
                bg="#34495e",
                relief=tk.FLAT,
                anchor="w",
                padx=20,
                activebackground=self.COLOR_ACCENT,
                activeforeground="white",
            )
            btn.pack(fill=tk.X, pady=2)

    def create_main_content(self):
        """Создание основной рабочей области"""
        main_frame = tk.Frame(self, bg=self.COLOR_BG, padx=20, pady=20)
        main_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Заголовок страницы
        title_label = tk.Label(
            main_frame,
            text="Панель управления",
            font=("Arial", 18, "bold"),
            bg=self.COLOR_BG,
            fg="#333",
        )
        title_label.pack(anchor="w", pady=(0, 20))

        # --- Блок информационных карточек (Статистика) ---
        cards_frame = tk.Frame(main_frame, bg=self.COLOR_BG)
        cards_frame.pack(fill=tk.X, pady=(0, 20))

        stats = [
            ("Пользователи", "1,250", "#2ecc71"),
            ("Продажи", "$14,230", "#3498db"),
            ("Конверсия", "4.5%", "#e67e22"),
        ]

        for i, (name, value, color) in enumerate(stats):
            card = tk.Frame(
                cards_frame, bg=self.COLOR_CARD, bd=1, relief=tk.SOLID
            )
            card.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)

            # Цветной индикатор сверху карточки
            line = tk.Frame(card, bg=color, height=4)
            line.pack(fill=tk.X, side=tk.TOP)

            lbl_name = tk.Label(
                card, text=name, font=("Arial", 10), fg="#7f8c8d", bg=card["bg"]
            )
            lbl_name.pack(pady=(10, 5), padx=10, anchor="w")

            lbl_val = tk.Label(
                card, text=value, font=("Arial", 16, "bold"), bg=card["bg"]
            )
            lbl_val.pack(pady=(0, 10), padx=10, anchor="w")

        # --- Блок с таблицей данных ---
        table_frame = tk.Frame(main_frame, bg=self.COLOR_CARD, pading=10)
        table_frame.pack(fill=tk.BOTH, expand=True)

        table_title = tk.Label(
            table_frame,
            text="Последние транзакции",
            font=("Arial", 12, "bold"),
            bg=self.COLOR_CARD,
        )
        table_title.pack(anchor="w", pady=(5, 10))

        # Определение колонок таблицы
        columns = ("id", "user", "amount", "status")
        tree = ttk.Treeview(
            table_frame, columns=columns, show="headings", height=8
        )

        tree.heading("id", text="ID")
        tree.heading("user", text="Пользователь")
        tree.heading("amount", text="Сумма")
        tree.heading("status", text="Статус")

        tree.column("id", width=50, anchor="center")
        tree.column("user", width=200, anchor="w")
        tree.column("amount", width=100, anchor="e")
        tree.column("status", width=120, anchor="center")

        # Тестовые данные для демонстрации шаблона
        demo_data = [
            ("1024", "Иванов И.И.", "5,400 руб.", "Успешно"),
            ("1025", "Петров П.П.", "1,200 руб.", "В обработке"),
            ("1026", "Сидоров С.С.", "12,800 руб.", "Успешно"),
            ("1027", "Алексеев А.А.", "350 руб.", "Отклонено"),
        ]

        for row in demo_data:
            tree.insert("", tk.END, values=row)

        tree.pack(fill=tk.BOTH, expand=True)

    def logout(self):
        """Обработчик кнопки выхода"""
        if messagebox.askyesno(
            "Выход", "Вы действительно хотите выйти из системы?"
        ):
            self.destroy()


if __name__ == "__main__":
    app = AdminDashboard()
    app.mainloop()