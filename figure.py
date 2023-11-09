import math
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Square(Figure):
    def __init__(self, top_right, side):
        self.top_right = top_right
        self.side = side  # Use the setter method to set the side length

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value <= 0:
            raise ValueError("\x1b[31mSide length must be greater than 0\x1b[0m\n")
        self._side = value

    def perimeter(self):
        return round(4 * self.side, 2)

    def area(self):
        return round(self.side ** 2, 2)


class Rectangle(Figure):
    def __init__(self, top_right, bottom_left):
        self.top_right = top_right
        self.bottom_left = bottom_left

    def perimeter(self):
        length = abs(self.top_right[0] - self.bottom_left[0])
        width = abs(self.top_right[1] - self.bottom_left[1])
        return round(2 * (length + width), 2)

    def area(self):
        length = abs(self.top_right[0] - self.bottom_left[0])
        width = abs(self.top_right[1] - self.bottom_left[1])
        return round(length * width, 2)


class Circle(Figure):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("\x1b[31mRadius length must be greater than 0\x1b[0m\n")
        self._radius = value

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    def area(self):
        return round(math.pi * self.radius ** 2, 2)


def error_message(message):
    return f"\x1b[31m!!!!! Input correct figure details in such format: '{message}'\x1b[0m\n"


def get_and_process_figure_details(figure_details):
    figure, *params = figure_details.split()
    figure = figure.lower()
    start_point = list(map(float, params[1:3]))
    common_details_str = len(params[0]) >= 3 and len(params[3]) >= 3 if len(params) > 3 else False

    if figure == 'square':
        try:
            if len(params) == 5 and common_details_str:
                return Square(start_point, float(params[4]))
            else:
                raise ValueError(error_message('Square TopRight 1 1 Side 1'))
        except ValueError as e:
            raise ValueError(e)

    elif figure == 'rectangle':
        try:
            if len(params) == 6 and common_details_str:
                return Rectangle(start_point, list(map(float, params[4:])))
            else:
                raise ValueError(error_message('Rectangle TopRight 2 2 BottomLeft 1 1'))
        except ValueError as e:
            raise ValueError(e)

    elif figure == 'circle':
        try:
            if len(params) == 5 and common_details_str:
                return Circle(start_point, float(params[4]))
            else:
                raise ValueError(error_message('Circle Center 1 1 Radius 2'))
        except ValueError as e:
            raise ValueError(e)
    else:
        raise ValueError(f'\x1b[31mOoops, we can not procces {figure} figure. \nPlease enter one of the supported shape types: Square, Rectangle, Circle\x1b[0m\n')


def main():
    while True:
        try:
            figure_details = input(f"Enter figure info. In one of such format\n"
                               f'{"-"*40}\n'
                               f"'Square TopRight 1 1 Side 1'\n"
                               f"'Rectangle TopRight 2 2 BottomLeft 1 1'\n"
                               f"'Circle Center 1 1 Radius 2':\n"                               
                               f'{"-"*40}\n')
            figure = get_and_process_figure_details(figure_details)
            print(f'{figure_details.split()[0]} Perimeter {figure.perimeter()} Area {figure.area()}\n')
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    main()
