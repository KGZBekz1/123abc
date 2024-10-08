# Базовый класс Figure
class Figure:
    unit = 'cm'  # единица измерения

    def init(self):
        pass

    def calculate_area(self):
        raise NotImplementedError("Этот метод должен быть переопределен в дочернем классе.")

    def info(self):
        raise NotImplementedError("Этот метод должен быть переопределен в дочернем классе.")

# Класс Square, наследуется от Figure
class Square(Figure):
    def __init__(self, side_length):
        super().init()
        self.__side_length = side_length  # приватный атрибут длины стороны

    def calculate_area(self):
        return self.__side_length ** 2  # площадь квадрата

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{self.unit}, area: {area}{self.unit}.")

# Класс Rectangle, наследуется от Figure
class Rectangle(Figure):
    def __init__(self, length, width):
        super().init()
        self.__length = length  # приватный атрибут длины
        self.__width = width    # приватный атрибут ширины

    def calculate_area(self):
        return self.__length * self.__width  # площадь прямоугольника

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit}, area: {area}{self.unit}.")

# Создание списка из двух квадратов и трех прямоугольников
shapes = [
    Square(5),   # Квадрат со стороной 5 см
    Square(7),   # Квадрат со стороной 7 см
    Rectangle(5, 8),  # Прямоугольник 5x8 см
    Rectangle(4, 10), # Прямоугольник 4x10 см
    Rectangle(6, 9)   # Прямоугольник 6x9 см
]

# Цикл для вывода информации о всех фигурах
for shape in shapes:
    shape.info()
