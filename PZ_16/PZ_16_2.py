# Создайте базовый класс "Человек" со свойствами "имя", "возраст" и "пол".
# От этого класса унаследуйте классы "Мужчина" и "Женщина" и добавьте в них
# свойства, связанные с социальным положением (например, "семейное положение",
# "количество детей" и т.д.).

class Person:


    def __init__(self, name: str, age: int, gender: str):

        self.name = name
        self.age = age
        self.gender = gender

    def get_base_info(self) -> str:
        return f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}"


class Man(Person):
    def __init__(self, name: str, age: int, military_service: bool):
        super().__init__(name, age, gender="Мужской")
        self.military_service = military_service

    def print_full_info(self):
        service_status = "Служил" if self.military_service else "Не служил"
        print(f"{self.get_base_info()}, Военная служба: {service_status}")


class Woman(Person):

    def __init__(self, name: str, age: int, marital_status: str, children_count: int):
        super().__init__(name, age, gender="Женский")
        self.marital_status = marital_status
        self.children_count = children_count

    def print_full_info(self):
        print(
            f"{self.get_base_info()}, "
            f"Семейное положение: {self.marital_status}, "
            f"Количество детей: {self.children_count}"
        )

if __name__ == "__main__":
    print("--- Тестирование Блока заданий 2 ---")
    man_example = Man(name="Александр", age=28, military_service=True)
    man_example.print_full_info()

    woman_example = Woman(
        name="Екатерина", age=32, marital_status="Замужем", children_count=2
    )
    woman_example.print_full_info()