class Computer:
    """Класс, представляющий компьютер и его основные характеристики."""

    def __init__(self, brand: str, processor: str, ram: int):
        """Инициализация атрибутов компьютера.

        :param brand: Марка (производитель) компьютера
        :param processor: Модель процессора
        :param ram: Объем оперативной памяти в ГБ
        """
        self.brand = brand
        self.processor = processor
        self.ram = ram

    def print_info(self):
        """Выводит структурированную информацию о компьютере на экран."""
        print(
            f"Марка: {self.brand}, "
            f"Процессор: {self.processor}, "
            f"Оперативная память: {self.ram} ГБ"
        )


# Тестовый запуск для Блока 1
if __name__ == "__main__":
    print("--- Тестирование Блока заданий 1 ---")
    # Создание экземпляров класса Компьютер
    pc_1 = Computer("ASUS", "Intel Core i7", 16)
    pc_2 = Computer("Apple MacBook", "Apple M2", 8)

    # Демонстрация работы метода вывода информации
    pc_1.print_info()
    pc_2.print_info()
    print()