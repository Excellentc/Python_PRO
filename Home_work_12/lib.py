"""
Доопрацюйте класс Pоint з наняття наступним чином: додайте перевірку координат x та y на числа за допомогою property
Доопрацюйте класс Дшту з наняття наступним чином: додайте можливість порівнювати лінії по довжині
(==, !=, >=, <=, >, <) за допомогою відповідних методів
"""


class Point:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('X not INT')
        else:
            self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('Y not INT')
        else:
            self._y = value


class Line:
    begin = None
    end = None

    def __init__(self, begin_point, end_point):
        self.begin = begin_point
        self.end = end_point
        self.length = self.calculation_length

    @property
    def calculation_length(self):
        k1 = self.begin.x - self.end.x
        k2 = self.begin.y - self.end.y

        res = (k1 ** 2 + k2 ** 2) ** 0.5

        return res

    def __gt__(self, other):
        return self.length > other.length

    def __lt__(self, other):
        return self.length < other.length

    def __ne__(self, other):
        return self.length != other.length

    def __eq__(self, other):
        return self.length == other.length

    def __le__(self, other):
        return self.length <= other.length

    def __ge__(self, other):
        return self.length >= other.length


point1_line1 = Point(1, 4)
point2_line1 = Point(21, 6)
line_one = Line(point1_line1, point2_line1)

point1_line2 = Point(0, 0)
point2_line2 = Point(2, 2)
line_two = Line(point1_line2, point2_line2)
