# Абстрактный класс для описания стола
class Table:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    def get_dimensions(self) -> str:
        """
        Возвращает размеры стола в формате "высота x ширина"
        """
        ...

    def calculate_area(self) -> float:
        """
        Вычисляет площадь стола
        """
        ...

    def describe_material(self) -> str:
        """
        Описывает материал, из которого сделан стол
        """
        ...

# Абстрактный класс для описания дерева
class Tree:
    def __init__(self, height: int, species: str):
        self.height = height
        self.species = species

    def get_height(self) -> int:
        """
        Возвращает высоту дерева
        """
        ...

    def get_species(self) -> str:
        """
        Возвращает вид дерева
        """
        ...

    def calculate_age(self) -> int:
        """
        Вычисляет возраст дерева
        """
        ...

# Абстрактный класс для описания стека
class Stack:
    def __init__(self, initial_size: int):
        self.size = initial_size
        self.items = []

    def push(self, item: str) -> None:
        """
        Добавляет элемент в стек
        """
        ...

    def pop(self) -> str:
        """
        Извлекает элемент из стека
        """
        ...

    def peek(self) -> str:
        """
        Возвращает верхний элемент стека без его удаления
        """
        ...

# Абстрактный класс для описания Facebook
class Facebook:
    def __init__(self, user_id: int, password: str):
        self.user_id = user_id
        self.password = password

    def login(self) -> bool:
        """
        Попытка входа в аккаунт Facebook
        """
        ...

    def post_message(self, message: str) -> None:
        """
        Публикует сообщение на стене пользователя
        """
        ...

    def get_friends(self) -> list:
        """
        Получает список друзей пользователя
        """
        ...

# Примеры использования методов
# Пример 1: Получение размеров стола
table = Table(100, 50)
print(table.get_dimensions())

# Пример 2: Расчет площади стола
print(table.calculate_area())

# Пример 3: Получение высоты дерева
tree = Tree(10, "Oak")
print(tree.get_height())

# Пример 4: Расчет возраста дерева
print(tree.calculate_age())

# Пример 5: Добавление элемента в стек
stack = Stack(10)
stack.push("Hello")
print(stack.peek())

# Пример 6: Извлечение элемента из стека
print(stack.pop())

# Пример 7: Вход в Facebook
fb = Facebook(123456789, "mypassword")
print(fb.login())

# Пример 8: Публикация сообщения на Facebook
fb.post_message("Привет, мир!")

# Пример 9: Получение списка друзей
print(fb.get_friends())