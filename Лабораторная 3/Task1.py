class Animal:
    """
    Базовый класс для всех животных.
    Атрибуты:
        name (str): Имя животного.
        age (int): Возраст животного.
        _species (str): Вид животного (инкапсулированный атрибут).
    """

    def __init__(self, name: str, age: int, species: str) -> None:
        """
        Конструктор базового класса Animal.
        :param name: Имя животного.
        :param age: Возраст животного.
        :param species: Вид животного.
        """
        self.name = name
        self.age = age
        self._species = species  # Инкапсулированный атрибут, так как вид животного не должен изменяться извне.

    def __str__(self) -> str:
        """
        Магический метод для строкового представления объекта.
        :return: Строка с описанием животного.
        """
        return f"{self.name} ({self._species}), возраст: {self.age} лет."

    def __repr__(self) -> str:
        """
        Магический метод для формального представления объекта.
        :return: Строка для отладки.
        """
        return f"Animal(name={self.name}, age={self.age}, species={self._species})"

    def make_sound(self) -> str:
        """
        Метод для издания звука животным.
        :return: Строка с описанием звука.
        """
        return "Неизвестный звук."


class Dog(Animal):
    """
    Дочерний класс Dog, наследуется от Animal.
    Атрибуты:
        breed (str): Порода собаки.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Конструктор дочернего класса Dog.
        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age, species="Собака")
        self.breed = breed

    def __str__(self) -> str:
        """
        Перегрузка магического метода для строкового представления объекта.
        :return: Строка с описанием собаки.
        """
        return f"{self.name} ({self._species}, порода: {self.breed}), возраст: {self.age} лет."

    def __repr__(self) -> str:
        """
        Перегрузка магического метода для формального представления объекта.
        :return: Строка для отладки.
        """
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

    def make_sound(self) -> str:
        """
        Перегрузка метода для издания звука собакой.
        :return: Строка с описанием звука.
        """
        return "Гав-гав!"

    def fetch(self, item: str) -> str:
        """
        Метод, специфичный для собак.
        :param item: Предмет, который нужно принести.
        :return: Строка с описанием действия.
        """
        return f"{self.name} приносит {item}."


class Cat(Animal):
    """
    Дочерний класс Cat, наследуется от Animal.
    Атрибуты:
        color (str): Цвет кошки.
    """

    def __init__(self, name: str, age: int, color: str) -> None:
        """
        Конструктор дочернего класса Cat.
        :param name: Имя кошки.
        :param age: Возраст кошки.
        :param color: Цвет кошки.
        """
        super().__init__(name, age, species="Кошка")
        self.color = color

    def __str__(self) -> str:
        """
        Перегрузка магического метода для строкового представления объекта.
        :return: Строка с описанием кошки.
        """
        return f"{self.name} ({self._species}, цвет: {self.color}), возраст: {self.age} лет."

    def __repr__(self) -> str:
        """
        Перегрузка магического метода для формального представления объекта.
        :return: Строка для отладки.
        """
        return f"Cat(name={self.name}, age={self.age}, color={self.color})"

    def make_sound(self) -> str:
        """
        Перегрузка метода для издания звука кошкой.
        :return: Строка с описанием звука.
        """
        return "Мяу!"

    def climb(self, height: float) -> str:
        """
        Метод, специфичный для кошек.
        :param height: Высота, на которую нужно забраться.
        :return: Строка с описанием действия.
        """
        return f"{self.name} забирается на высоту {height} метров."


# Пример использования
animal = Animal("Неизвестное животное", 5, "Неизвестный вид")
print(animal)
print(repr(animal))
print(animal.make_sound())

dog = Dog("Бобик", 3, "Лабрадор")
print(dog)
print(repr(dog))
print(dog.make_sound())
print(dog.fetch("мячик"))

cat = Cat("Мурка", 2, "рыжий")
print(cat)
print(repr(cat))
print(cat.make_sound())
print(cat.climb(2.5))