from typing import Self

class Shape:
    def set_scale(self, scale: float) -> Self:
        self.scale = scale
        return self

class Circle(Shape):
    def set_radius(self, radius: float) -> Self:
        self.radius = radius
        return self

print(type(Circle().set_scale(0.5)))
print(type(Circle().set_scale(0.5).set_radius(2.7)))
