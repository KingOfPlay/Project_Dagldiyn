import sqlite3

def insert_initial_data():
    initial_products = [
        ("Apple iPhone 14", "Смартфон", 75000, 20, 5),
        ("Samsung Galaxy S23", "Смартфон", 65000, 15, 5),
        ("Sony WH-1000XM5", "Наушники", 30000, 10, 3),
        ("Xiaomi Mi Band 8", "Фитнес-браслет", 3500, 50, 10),
        ("Logitech MX Master 3S", "Мышь", 12000, 8, 2),
        ("Asus ROG Strix G15", "Ноутбук", 120000, 5, 2),
        ("iPad Pro 11", "Планшет", 90000, 7, 3),
        ("HyperX Cloud II", "Наушники", 10000, 12, 4),
        ("Canon EOS 2000D", "Фотоаппарат", 45000, 4, 2),
        ("Seagate 1TB HDD", "Жесткий диск", 5000, 25, 5)
    ]

    with sqlite3.connect("stock.db") as conn:
        cursor = conn.cursor()
        cursor.executemany("""
            INSERT INTO products (trade_mark, type, price, quantity_in_stock, minimum_stock)
            VALUES (?, ?, ?, ?, ?)
        """, initial_products)
        conn.commit()