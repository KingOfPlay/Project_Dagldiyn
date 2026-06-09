class Person:
    """Базовый класс, описывающий человека."""

    def __init__(self, name: str, age: int, gender: str):
        """Инициализация общих свойств человека.

        :param name: Имя человека
        :param age: Возраст в годах
        :param gender: Пол (например, 'Мужской' или 'Женский')
        """
        self.name = name
        self.age = age
        self.gender = gender

    def get_base_info(self) -> str:
        """Возвращает строку с базовой информацией о человеке."""
        return f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}"


class Man(Person):
    """Класс 'Мужчина', наследующий свойства класса Person."""

    def __init__(self, name: str, age: int, military_service: bool):
        """Инициализация свойств мужчины, включая социальное/специфичное свойство.

        :param military_service: Прохождение военной службы (True/False)
        """
        # Вызов конструктора базового класса
        super().__init__(name, age, gender="Мужской")
        self.military_service = military_service

    def print_full_info(self):
        """Выводит полную информацию о мужчине."""
        service_status = "Служил" if self.military_service else "Не служил"
        print(f"{self.get_base_info()}, Военная служба: {service_status}")


class Woman(Person):
    """Класс 'Женщина', наследующий свойства класса Person."""

    def __init__(self, name: str, age: int, marital_status: str, children_count: int):
        """Инициализация свойств женщины, включая социальное положение.

        :param marital_status: Семейное положение (строка)
        :param children_count: Количество детей
        """
        # Вызов конструктора базового класса
        super().__init__(name, age, gender="Женский")
        self.marital_status = marital_status
        self.children_count = children_count

    def print_full_info(self):
        """Выводит полную информацию о женщине."""
        print(
            f"{self.get_base_info()}, "
            f"Семейное положение: {self.marital_status}, "
            f"Количество детей: {self.children_count}"
        )


# Тестовый запуск для Блока 2
if __name__ == "__main__":
    print("--- Тестирование Блока заданий 2 ---")
    # Создание объекта класса Мужчина
    man_example = Man(name="Александр", age=28, military_service=True)
    man_example.print_full_info()

    # Создание объекта класса Женщина
    woman_example = Woman(
        name="Екатерина", age=32, marital_status="Замужем", children_count=2
    )
    woman_example.print_full_info()