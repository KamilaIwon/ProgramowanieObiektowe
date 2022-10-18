import math
class Point(object):
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'<{self.x}, {self.y}>'

    def move(self, delta_x: float, delta_y: float) -> None:
        self.x += delta_x
        self.y += delta_y

    @staticmethod
    def distance(p1, p2 ) -> float:
        return math.sqrt(((p2.x - p1.x) ** 2) + ((p2.y - p1.y) ** 2))


