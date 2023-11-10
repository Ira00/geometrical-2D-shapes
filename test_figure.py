from figure import *


def test_square_perimeter():
    square = Square(['TopRight', '1', '1', 'Side', '2'])
    assert square.perimeter() == 8.0


def test_square_area():
    square = Square(['TopRight', '1', '1', 'Side', '2'])
    assert square.area() == 4.0


def test_rectangle_perimeter():
    rectangle = Rectangle(['TopRight', '2', '2', 'BottomLeft', '1', '1'])
    assert rectangle.perimeter() == 4.0


def test_rectangle_area():
    rectangle = Rectangle(['TopRight', '2', '2', 'BottomLeft', '1', '1'])
    assert rectangle.area() == 1.0


def test_circle_perimeter():
    circle = Circle(['Center', '1', '1', 'Radius', '2'])
    assert circle.perimeter() == 12.57


def test_circle_area():
    circle = Circle(['Center', '1', '1', 'Radius', '2'])
    assert circle.area() == 12.57


def test_error_message():
    message = Figure.error_message('Square TopRight 1 1 Side 1')
    assert message == "\x1b[31m!!!!! Input correct figure details in such format: 'Square TopRight 1 1 Side 1'\x1b[0m\n"


def test_get_and_process_figure_details_square():
    figure_details = "Square TopRight 1 1 Side 1"
    figure = get_and_process_figure_details(figure_details)
    assert isinstance(figure, Square)


def test_get_and_process_figure_details_square_error():
    figure_details = "Square TopRight 1 1 Side "
    try:
        figure = get_and_process_figure_details(figure_details)
        assert False
    except ValueError as e:
        assert str(e) == Figure.error_message('Square TopRight 1 1 Side 1')


def test_get_and_process_figure_details_square_side_error():
    figure_details = "Square TopRight 1 1 Side -1"
    try:
        figure = get_and_process_figure_details(figure_details)
        assert False
    except ValueError as e:
        assert 'Side length must be greater than 0' in str(e)


def test_get_and_process_figure_details_rectangle():
    figure_details = "Rectangle TopRight 2 2 BottomLeft 1 1"
    figure = get_and_process_figure_details(figure_details)
    assert isinstance(figure, Rectangle)


def test_get_and_process_figure_details_rectangle_error():
    figure_details = "Rectangle TopRight 2 2 11 1 1"
    try:
        figure = get_and_process_figure_details(figure_details)
        assert False
    except ValueError as e:
        assert str(e) == Figure.error_message('Rectangle TopRight 2 2 BottomLeft 1 1')


def test_get_and_process_figure_details_circle():
    figure_details = "Circle Center 1 1 Radius 2"
    figure = get_and_process_figure_details(figure_details)
    assert isinstance(figure, Circle)


def test_get_and_process_figure_details_circle_error():
    figure_details = "Circle c 1 1 Radius 2"
    try:
        figure = get_and_process_figure_details(figure_details)
        assert False
    except ValueError as e:
        assert str(e) == Figure.error_message('Circle Center 1 1 Radius 2')


def test_get_and_process_figure_details_circle_radius_error():
    figure_details = "Circle Center 1 1 Radius 0"
    try:
        figure = get_and_process_figure_details(figure_details)
        assert False
    except ValueError as e:
        assert 'Radius length must be greater than 0' in str(e)


def test_get_and_process_figure_details_error_figure():
    figure_details = "Apple Center 1 1 Radius 2"
    try:
        figure = get_and_process_figure_details(figure_details)
        assert False
    except ValueError as e:
        assert 'Ooops' in str(e)
