# class MyCar:
#     wheels = 4
#
#     def __init__(self, wheels_count):
#         self.wheels = wheels_count
#
#     def ride(self):
#         print('In ride method')
#
#
# car = MyCar(3)
# car1 = MyCar(4)
#
#
# print(car)
#
# car.ride()
# print(car.wheels)


# class Point:
#     x = None
#     y = None
#
#     def __init__(self, x_coord, y_coord):
#         # check type
#         self.x = x_coord
#         self.y = y_coord
#
#
# point1 = Point(0, 0)
# point2 = Point(10, 10)
#
#
# class Line:
#     begin = None
#     end = None
#
#     def __init__(self, begin_point, end_point):
#         self.begin = begin_point
#         self.end = end_point
#
#     def __str__(self):
#         return f'Line with coords [{self.begin.x}-{self.begin.y}:{self.end.x}-{self.end.y}]'
#
#     def __bool__(self):
#         return True
#
#
# line1 = Line(point1, point2)
#
# my_str = str(line1)
# print(my_str)
#
# print(bool(line1))
#
# if line1:  # bool(line1)
#     pass
#
# # line1 = point1 + point2
#

#
# class Point:
#     x = None
#     y = None
#
#     def __init__(self, x_coord, y_coord):
#         # check type
#         self.x = x_coord
#         self.y = y_coord
#
#     def __eq__(self, other):  # ==
#         if not isinstance(other, type(self)):
#             raise TypeError
#
#         is_x_match = self.x == other.x
#         is_y_match = self.y == other.y
#
#         return is_x_match and is_y_match
#
#     def __ne__(self, other):  # !=
#         return True
#
#     def __lt__(self, other):  # <
#         return True
#
#     def __le__(self, other):  # <=
#         return True
#
#     def __gt__(self, other):  # >
#         return True
#
#     def __ge__(self, other):  # >=
#         return True
#
#     def __add__(self, other):  # +
#         print('In add')
#         return Line(self, other)
#
#
# point1 = Point(10, 10)
# point2 = Point(10, 10)
#
# if point1 == point2:
#     print('Match!')
#
#
# class Line:
#     begin = None
#     end = None
#
#     def __init__(self, begin_point, end_point):
#         self.begin = begin_point
#         self.end = end_point
#
#     def __str__(self):
#         return f'Line with coords [{self.begin.x}-{self.begin.y}:{self.end.x}-{self.end.y}]'
#
#
# line1 = point1 + point2
#
# print(line1)

#
# class Point:
#     x = None
#     y = None
#
#     def __init__(self, x_coord, y_coord):
#         # check type
#         self.x = x_coord
#         self.y = y_coord
#
#     def __getattribute__(self, item):
#         print('__getattribute__', item)
#         return super().__getattribute__(item)
#
#     def __getattr__(self, item):
#         print('__getattr__', item)
#         print('self.__dict__', self.__dict__)
#         print('self.__class__.__dict__', self.__class__.__dict__)
#         try:
#             self.__dict__.get(item) or self.__class__.__dict__.get(item)
#         except Exception:
#             raise AttributeError(f'No match: {item}')
#
#     def __setattr__(self, key, value):
#         print('__setattr__', key, value)
#
#         self.__dict__[key] = value
#
#
# point = Point(1, 2)
# point2 = Point(1, 2)
#
#
# print(point.x)
# print(point.y)
# # print(point.ysdfgh)
# point.ysdfgh = 10
#
# print(point.x)
# print(point.ysdfgh)


# class Point:
#     x = None
#     y = None
#
#     def __init__(self, x_coord, y_coord):
#         # check type
#         self.x = x_coord
#         self.y = y_coord
#
#
# class Line:
#     begin = None
#     end = None
#
#     def __init__(self, begin_point, end_point):
#         self.begin = begin_point
#         self.end = end_point
#
#     def __str__(self):
#         return f'Line with coords [{self.begin.x}-{self.begin.y}:{self.end.x}-{self.end.y}]'
#
#     def __getitem__(self, item):
#         print('__getitem__', item)
#         value = self.__dict__.get(item)
#         return value
#
#     def __setitem__(self, key, value):
#         print('__setitem__', key, value)
#         self.__dict__[key] = value
#
#
# point = Point(1, 2)
# point2 = Point(1, 2)
#
# line = Line(point, point2)
#
# print(line[0])
# print(line['dsvfgh'])
#
# line[0] = 10
# print(line[0])

#
# class Point:
#     _x = None
#     x = None
#     y = None
#
#     def __init__(self, x_coord, y_coord):
#         # check type
#         self.x = x_coord
#         self.y = y_coord
#
#
# class Line:
#     begin = None
#     end = None
#
#     def __init__(self, begin_point, end_point):
#         self.begin = begin_point
#         self.end = end_point
#         self.length = self._length()
#
#     def __str__(self):
#         return f'Line with coords [{self.begin.x}-{self.begin.y}:{self.end.x}-{self.end.y}]'
#
#     def _length(self):
#
#         k1 = self.begin.x - self.end.x
#         k2 = self.begin.y - self.end.y
#
#         res = (k1 ** 2 + k2 ** 2) ** 0.5
#
#         return res
#
#
# p1 = Point(0, 0)
# p2 = Point(2, 2)
#
# line = Line(p1, p2)
#
# print(line._length())
#
# p2.x = 4
#
# print(line._length())
# print(line.length)

#
# class Point:
#     x = None
#     y = None
#
#     def __init__(self, x_coord, y_coord):
#         # check type
#         self.x = x_coord
#         self.y = y_coord
#
#
# class Line:
#     begin = None
#     end = None
#
#     def __init__(self, begin_point, end_point):
#         self.begin = begin_point
#         self.end = end_point
#
#     def __str__(self):
#         return f'Line with coords [{self.begin.x}-{self.begin.y}:{self.end.x}-{self.end.y}]'
#
#     def length_getter(self):
#         print('length_getter')
#
#         k1 = self.begin.x - self.end.x
#         k2 = self.begin.y - self.end.y
#
#         res = (k1 ** 2 + k2 ** 2) ** 0.5
#
#         return res
#
#     def length_setter(self, value):
#         print('length_setter', value)
#
#     length = property(length_getter, length_setter)
#
#
# p1 = Point(0, 0)
# p2 = Point(2, 2)
#
# line = Line(p1, p2)
#
# print(line.length)
# print(type(line.length))
#
# line.length = 10


# class Point:
#     x = None
#     y = None
#
#     def __init__(self, x_coord, y_coord):
#         # check type
#         self.x = x_coord
#         self.y = y_coord
#
#
# class Line:
#     begin = None
#     end = None
#
#     def __init__(self, begin_point, end_point):
#         self.begin = begin_point
#         self.end = end_point
#
#     def __str__(self):
#         return f'Line with coords [{self.begin.x}-{self.begin.y}:{self.end.x}-{self.end.y}]'
#
#     length = property()
#
#     @length.getter
#     def length(self):
#         print('length_getter')
#
#         k1 = self.begin.x - self.end.x
#         k2 = self.begin.y - self.end.y
#
#         res = (k1 ** 2 + k2 ** 2) ** 0.5
#
#         return res
#
#     @length.setter
#     def length(self, value):
#         print('length_setter', value)
#

# p1 = Point(0, 0)
# p2 = Point(2, 2)
#
# line = Line(p1, p2)
#
# print(line.length)
# print(type(line.length))
#
# line.length = 10

#
# class Point:
#     x = None
#     y = None
#
#     def __init__(self, x_coord, y_coord):
#         # check type
#         self.x = x_coord
#         self.y = y_coord
#
#
# class Line:
#     begin = None
#     end = None
#
#     def __init__(self, begin_point, end_point):
#         self.begin = begin_point
#         self.end = end_point
#
#     def __str__(self):
#         return f'Line with coords [{self.begin.x}-{self.begin.y}:{self.end.x}-{self.end.y}]'
#
#     @property  # getter
#     def length(self):
#         print('length_getter')
#
#         k1 = self.begin.x - self.end.x
#         k2 = self.begin.y - self.end.y
#
#         res = (k1 ** 2 + k2 ** 2) ** 0.5
#
#         return res
#
#
# p1 = Point(0, 0)
# p2 = Point(2, 2)
#
# line = Line(p1, p2)
#
# print(line.length)
# print(type(line.length))


#
# class Example:
#
#     class_arg = 54321
#
#     def __init__(self, val):
#         self.class_arg = val
#
#     def from_object_method(self):
#         print(self)
#         print(self.class_arg)
#
#     # def from_class_method(self):
#     #     print(self.__class__.class_arg)
#
#     @classmethod
#     def from_class_method(cls):
#         print(cls)
#         print(cls.class_arg)
#
#     @staticmethod
#     def method():
#         print('Just method')
#
#
# ex = Example(123)
#
# ex.from_object_method()
#
# ex.from_class_method()
# ex.method()


# from abc import ABC, abstractmethod
#
#
# class User(ABC):
#
#     @abstractmethod
#     def do_smth(self):
#         pass
#
#
# class Admin(User):
#
#     def do_smth(self):
#         pass
#
#
# # user = User()
#
# admin = Admin()
