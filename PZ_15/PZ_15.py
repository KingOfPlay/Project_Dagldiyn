# Приложение ТОВАРНЫЙ ЗАПАС для автоматизированного учета товарных
# запасов на складе. БД должна содержать таблицу Товары со следующей
# структурой записи: Код товара, Торговая марка, Тип, Цена,
# Количество на складе, Минимальный запас.

# Приложение ТОВАРНЫЙ ЗАПАС для автоматизированного учета товарных запасов на складе.
# БД должна содержать таблицу Товары со следующей структурой записи:
# Код товара, Торговая марка, Тип, Цена, Количество на складе, Минимальный запас.

import sqlite3
from data import insert_initial_data

DB_NAME = "stock.db"


def print_table(title, rows):
    print(f"\n--- {title} ---")
    for row in rows:
        print(row)


# Создание таблицы
with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trade_mark TEXT NOT NULL,
            type TEXT NOT NULL,
            price REAL NOT NULL,
            quantity_in_stock INTEGER NOT NULL,
            minimum_stock INTEGER NOT NULL
        )
    """)

# Добавление начальных данных (10 позиций)
insert_initial_data()

# Основные операции
with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()

    # 1. Исходное состояние
    cursor.execute("SELECT * FROM products")
    print_table("Исходное состояние базы данных", cursor.fetchall())

    # 2. ПОИСК (3 разных запроса)

    # Поиск товаров с ценой > 50000
    cursor.execute("SELECT * FROM products WHERE price > 50000")
    print_table("Поиск: товары дороже 50000 руб.", cursor.fetchall())

    # Поиск товаров, количество на складе меньше минимального запаса
    cursor.execute("SELECT * FROM products WHERE quantity_in_stock < minimum_stock")
    print_table("Поиск: товары с недостаточным запасом", cursor.fetchall())

    # Поиск товаров определенного типа
    cursor.execute("SELECT * FROM products WHERE type = 'Наушники'")
    print_table("Поиск: товары типа 'Наушники'", cursor.fetchall())

    # 3. РЕДАКТИРОВАНИЕ (3 разных запроса)

    # Увеличить цену всех смартфонов на 5%
    cursor.execute("UPDATE products SET price = price * 1.05 WHERE type = 'Смартфон'")

    # Уменьшить количество на складе для товаров, где оно больше 20
    cursor.execute("UPDATE products SET quantity_in_stock = quantity_in_stock - 5 WHERE quantity_in_stock > 20")

    # Обновить минимальный запас до 10 для товаров с типом 'Наушники'
    cursor.execute("UPDATE products SET minimum_stock = 10 WHERE type = 'Наушники'")

    conn.commit()

    cursor.execute("SELECT * FROM products")
    print_table("Состояние после операций редактирования", cursor.fetchall())

    # 4. УДАЛЕНИЕ (3 разных запроса)

    # Удалить товары с количеством на складе = 0 (хотя у нас нет нулевых, для примера)
    cursor.execute("DELETE FROM products WHERE quantity_in_stock = 0")

    # Удалить товары с ценой менее 10000 руб.
    cursor.execute("DELETE FROM products WHERE price < 10000")

    # Удалить товары, у которых минимальный запас больше 8
    cursor.execute("DELETE FROM products WHERE minimum_stock > 8")

    conn.commit()

    cursor.execute("SELECT * FROM products")
    print_table("Состояние после операций удаления", cursor.fetchall())