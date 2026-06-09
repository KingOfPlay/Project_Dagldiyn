# Создайте класс "Компьютер" с атрибутами "марка", "процессор" и "оперативная
# память". Напишите метод, который выводит информацию о компьютере в формате
# "Марка: марка, Процессор: процессор, Оперативная память: память".

class Computer:

    def __init__(self, brand: str, processor: str, ram: int):
        self.brand = brand
        self.processor = processor
        self.ram = ram

    def print_info(self):
        print(
            f"Марка: {self.brand}, "
            f"Процессор: {self.processor}, "
            f"Оперативная память: {self.ram} ГБ"
        )

if __name__ == "__main__":
    print("--- Тестирование Блока заданий 1 ---")
    pc_1 = Computer("ASUS", "Intel Core i7", 16)
    pc_2 = Computer("Apple MacBook", "Apple M2", 8)

    pc_1.print_info()
    pc_2.print_info()
    print()