# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk.
# Получить интерфейс максимально приближенный к оригиналу
import tkinter as tk
from tkinter import messagebox, ttk


def on_exit():
    if messagebox.askyesno("Выход", "Вы действительно хотите выйти?"):
        root.destroy()


root = tk.Tk()
root.title("HTML5 Admin Template - Dashboard")
root.geometry("950x600")
root.configure(bg="#f4f6f9")

header_frame = tk.Frame(root, bg="#2c3e50", height=50)
header_frame.pack(side=tk.TOP, fill=tk.X)
header_frame.pack_propagate(False)

logo_label = tk.Label(
    header_frame,
    text="ADMIN COMPASS",
    font=("Arial", 13, "bold"),
    fg="#ffffff",
    bg="#2c3e50",
)
logo_label.pack(side=tk.LEFT, padx=15, pady=12)

exit_btn = tk.Button(
    header_frame,
    text="Выйти",
    bg="#3498db",
    fg="white",
    relief=tk.FLAT,
    font=("Arial", 10),
    command=on_exit,
)
exit_btn.pack(side=tk.RIGHT, padx=15, pady=10)

sidebar_frame = tk.Frame(root, bg="#34495e", width=180)
sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
sidebar_frame.pack_propagate(False)

menu_items = ["📊 Dashboard", "📈 Analytics", "👥 Users", "📦 Products", "⚙️ Settings"]
for item in menu_items:
    btn = tk.Button(
        sidebar_frame,
        text=item,
        font=("Arial", 11),
        fg="#bdc3c7",
        bg="#34495e",
        relief=tk.FLAT,
        anchor="w",
        padx=15,
        activebackground="#3498db",
        activeforeground="white",
    )
    btn.pack(fill=tk.X, pady=2)

content_frame = tk.Frame(root, bg="#f4f6f9", padx=20, pady=20)
content_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

page_title = tk.Label(
    content_frame,
    text="Панель мониторинга",
    font=("Arial", 16, "bold"),
    bg="#f4f6f9",
    fg="#333333",
)
page_title.pack(anchor="w", pady=(0, 15))

cards_container = tk.Frame(content_frame, bg="#f4f6f9")
cards_container.pack(fill=tk.X, pady=(0, 20))

cards_data = [
    ("Новые заказы", "154", "#2ecc71"),
    ("Выручка", "45,200 ₽", "#3498db"),
    ("Конверсия", "4.8%", "#e67e22"),
]

for title, val, color in cards_data:
    card = tk.Frame(cards_container, bg="#ffffff", bd=1, relief=tk.SOLID)
    card.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)

    top_bar = tk.Frame(card, bg=color, height=4)
    top_bar.pack(fill=tk.X, side=tk.TOP)

    l_title = tk.Label(
        card, text=title, font=("Arial", 10), fg="#7f8c8d", bg="#ffffff"
    )
    l_title.pack(pady=(8, 2), padx=10, anchor="w")

    l_val = tk.Label(
        card, text=val, font=("Arial", 14, "bold"), fg="#2c3e50", bg="#ffffff"
    )
    l_val.pack(pady=(0, 8), padx=10, anchor="w")

table_container = tk.Frame(content_frame, bg="#ffffff", bd=1, relief=tk.SOLID)
table_container.pack(fill=tk.BOTH, expand=True)

table_title = tk.Label(
    table_container,
    text="Последняя активность",
    font=("Arial", 11, "bold"),
    bg="#ffffff",
    fg="#2c3e50",
)
table_title.pack(anchor="w", pady=(0, 10))

columns = ("id", "customer", "amount", "status")
tree = ttk.Treeview(table_container, columns=columns, show="headings", height=8)

tree.heading("id", text="ID")
tree.heading("customer", text="Контрагент")
tree.heading("amount", text="Сумма")
tree.heading("status", text="Статус")

tree.column("id", width=60, anchor="center")
tree.column("customer", width=220, anchor="w")
tree.column("amount", width=110, anchor="e")
tree.column("status", width=110, anchor="center")

demo_rows = [
    ("0041", "ООО Вектор", "12,400 ₽", "Обработано"),
    ("0042", "ИП Петров А.В.", "3,150 ₽", "В ожидании"),
    ("0043", "Соколова М.Н.", "850 ₽", "Обработано"),
    ("0044", "ЗАО Технолоджи", "94,000 ₽", "Отклонено"),
]

for row in demo_rows:
    tree.insert("", tk.END, values=row)

tree.pack(fill=tk.BOTH, expand=True)

root.mainloop()