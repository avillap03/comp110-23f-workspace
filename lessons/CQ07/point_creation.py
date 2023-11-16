"""testing Points class."""

from lessons.CQ07.point import Point

my_point: Point = Point(3.5, 7.0)

print(my_point.scale_by(2))
print(my_point.scale(3))