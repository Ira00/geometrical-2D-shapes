import math
from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, params):
        if len(params) != self.PARAMS_COUNT or not self.common_details_str(params):
            raise ValueError(self.error_message(self.ERROR_MESSAGE))

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def common_details_str(self, params):
        return len(params[0]) >= 3 and len(params[3]) >= 3 if len(params) > 3 else False

    @staticmethod
    def error_message(message):
        return f"\x1b[31m!!!!! Input correct figure details in such format: '{message}'\x1b[0m\n"


class Square(Figure):
    PARAMS_COUNT = 5
    ERROR_MESSAGE = 'Square TopRight 1 1 Side 1'

    def __init__(self, params):
        super().__init__(params)
        self.top_right = list(map(float, params[1:3]))
        self.side = float(params[4])

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
    PARAMS_COUNT = 6
    ERROR_MESSAGE = 'Rectangle TopRight 2 2 BottomLeft 1 1'

    def __init__(self, params):
        super().__init__(params)
        self.top_right = list(map(float, params[1:3]))
        self.bottom_left = list(map(float, params[4:]))

    def perimeter(self):
        length = abs(self.top_right[0] - self.bottom_left[0])
        width = abs(self.top_right[1] - self.bottom_left[1])
        return round(2 * (length + width), 2)

    def area(self):
        length = abs(self.top_right[0] - self.bottom_left[0])
        width = abs(self.top_right[1] - self.bottom_left[1])
        return round(length * width, 2)


class Circle(Figure):
    PARAMS_COUNT = 5
    ERROR_MESSAGE = 'Circle Center 1 1 Radius 2'

    def __init__(self, params):
        super().__init__(params)
        self.center = list(map(float, params[1:3]))
        self.radius = float(params[4])

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





def get_and_process_figure_details(figure_details):
    figure, *params = figure_details.split()
    figure = figure.lower()

    figure_dict = {
        'square': Square,
        'rectangle': Rectangle,
        'circle': Circle
    }

    if figure in figure_dict:
        return figure_dict[figure](params)
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
