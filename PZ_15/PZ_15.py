import sqlite3
from sqlite3 import Error
from data import initial_items

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Ошибка при подключении к БД: {e}")
    return conn


def create_table(conn):
    try:
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS items (
            item_id INTEGER PRIMARY KEY,
            brand TEXT NOT NULL,
            item_type TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            min_stock INTEGER NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
        conn.commit()
    except Error as e:
        print(f"Ошибка при создании таблицы: {e}")


def seed_database(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM items")
    if cursor.fetchone()[0] == 0:
        try:
            cursor.executemany(
                "INSERT INTO items VALUES (?, ?, ?, ?, ?, ?);",
                initial_items
            )
            conn.commit()
            print("База данных успешно инициализирована 10 товарами.")
        except Error as e:
            print(f"Ошибка при заполнении БД: {e}")


# ввод данных
def insert_item(conn):
    print('\n', 'Добавление нового товара')
    try:
        item_id = int(input("Введите код товара (ID): "))
        brand = input("Введите торговую марку: ").strip()
        item_type = input("Введите тип товара: ").strip()
        price = float(input("Введите цену: "))
        quantity = int(input("Введите количество на складе: "))
        min_stock = int(input("Введите минимальный запас: "))

        if not brand or not item_type:
            print("Ошибка: Поля 'Торговая марка' и 'Тип' не могут быть пустыми.")
            return

        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO items VALUES (?, ?, ?, ?, ?, ?);",
            (item_id, brand, item_type, price, quantity, min_stock)
        )
        conn.commit()
        print("Товар успешно добавлен!")
    except ValueError:
        print("Ошибка ввода: Проверьте правильность типов данных (ID, количество, запас - целые; цена - дробное).")
    except Error as e:
        print(f"Ошибка БД (возможно, товар с таким ID уже существует): {e}")


# поиск
def search_menu(conn):
    print('\n', 'Режимы поиска')
    print("1. Поиск по типу товара (Запрос 1)")
    print("2. Поиск по торговой марке (Запрос 2)")
    print("3. Показать товары с дефицитом (Кол-во < Мин. запас) (Запрос 3)")

    choice = input("Выберите вариант поиска: ").strip()
    cursor = conn.cursor()

    try:
        if choice == '1':
            item_type = input("Введите тип товара для поиска: ").strip()
            cursor.execute("SELECT * FROM items WHERE item_type LIKE ?;", (f"%{item_type}%",))
        elif choice == '2':
            brand = input("Введите торговую марку для поиска: ").strip()
            cursor.execute("SELECT * FROM items WHERE brand LIKE ?;", (f"%{brand}%",))
        elif choice == '3':
            cursor.execute("SELECT * FROM items WHERE quantity < min_stock;")
        else:
            print("Неверный выбор.")
            return

        rows = cursor.fetchall()
        display_results(rows)
    except Error as e:
        print(f"Ошибка при выполнении поиска: {e}")


# редактирование
def edit_menu(conn):
    print('\n', 'Режимы редактирования')
    print("1. Изменить цену товара по ID (Запрос 1)")
    print("2. Изменить количество на складе по ID (Запрос 2)")
    print("3. Обновить минимальный запас для всего типа товаров (Запрос 3)")

    choice = input("Выберите вариант редактирования: ").strip()
    cursor = conn.cursor()

    try:
        if choice == '1':
            item_id = int(input("Введите ID товара: "))
            new_price = float(input("Введите новую цену: "))
            cursor.execute("UPDATE items SET price = ? WHERE item_id = ?;", (new_price, item_id))
        elif choice == '2':
            item_id = int(input("Введите ID товара: "))
            new_qty = int(input("Введите новое количество: "))
            cursor.execute("UPDATE items SET quantity = ? WHERE item_id = ?;", (new_qty, item_id))
        elif choice == '3':
            item_type = input("Введите тип товара: ").strip()
            new_min = int(input("Введите новый лимит минимального запаса: "))
            cursor.execute("UPDATE items SET min_stock = ? WHERE item_type = ?;", (new_min, item_type))
        else:
            print("Неверный выбор.")
            return

        conn.commit()
        if cursor.rowcount > 0:
            print(f"Данные успешно обновлены. Изменено строк: {cursor.rowcount}")
        else:
            print("Записи по указанным критериям не найдены.")
    except ValueError:
        print("Ошибка ввода: Некорректный формат чисел.")
    except Error as e:
        print(f"Ошибка при изменении данных: {e}")


# удаление
def delete_menu(conn):
    print('\n', 'Режимы удаления')
    print("1. Удалить товар по ID (Запрос 1)")
    print("2. Удалить все товары определенного типа (Запрос 2)")
    print("3. Удалить все товары определенного бренда (Запрос 3)")

    choice = input("Выберите вариант удаления: ").strip()
    cursor = conn.cursor()

    try:
        if choice == '1':
            item_id = int(input("Введите ID товара для удаления: "))
            cursor.execute("DELETE FROM items WHERE item_id = ?;", (item_id,))
        elif choice == '2':
            item_type = input("Введите тип товаров для удаления: ").strip()
            cursor.execute("DELETE FROM items WHERE item_type = ?;", (item_type,))
        elif choice == '3':
            brand = input("Введите торговую марку для удаления: ").strip()
            cursor.execute("DELETE FROM items WHERE brand = ?;", (brand,))
        else:
            print("Неверный выбор.")
            return

        conn.commit()
        if cursor.rowcount > 0:
            print(f"Удаление выполнено успешно. Удалено строк: {cursor.rowcount}")
        else:
            print("Записи для удаления не найдены.")
    except ValueError:
        print("Ошибка ввода: ID должен быть целым числом.")
    except Error as e:
        print(f"Ошибка при удалении данных: {e}")


def display_all_items(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items;")
        rows = cursor.fetchall()
        print("\n--- Весь товарный запас на складе ---")
        display_results(rows)
    except Error as e:
        print(f"Ошибка вывода данных: {e}")


def display_results(rows):
    if not rows:
        print("Записи не найдены.")
        return

    print(f"{'ID':<6} | {'Бренд':<12} | {'Тип товара':<15} | {'Цена':<10} | {'Кол-во':<8} | {'Мин. запас':<10}")
    print("-" * 75)
    for row in rows:
        print(f"{row[0]:<6} | {row[1]:<12} | {row[2]:<15} | {row[3]:<10.2f} | {row[4]:<8} | {row[5]:<10}")


def main():
    db_name = "inventory.db"
    conn = create_connection(db_name)

    if conn is not None:
        create_table(conn)
        seed_database(conn)

        while True:
            print('\n', 'Меню управления складом')
            print("1. Посмотреть все товары")
            print("2. Добавить новый товар (Ввод)")
            print("3. Поиск товаров (3 SQL-запроса)")
            print("4. Редактировать данные (3 SQL-запроса)")
            print("5. Удалить данные (3 SQL-запроса)")
            print("6. Выйти из программы")

            choice = input("Выберите действие (1-6): ").strip()

            if choice == '1':
                display_all_items(conn)
            elif choice == '2':
                insert_item(conn)
            elif choice == '3':
                search_menu(conn)
            elif choice == '4':
                edit_menu(conn)
            elif choice == '5':
                delete_menu(conn)
            elif choice == '6':
                print("Завершение работы программы. До свидания!")
                conn.close()
                break
            else:
                print("Некорректный ввод, пожалуйста, повторите попытку.")
    else:
        print("Критическая ошибка: невозможно создать подключение к базе данных.")


if __name__ == '__main__':
    main()