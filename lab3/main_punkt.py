from punkt_alfa import Point
from named_point import NamedPoint

def main():
    a: Point = Point(5, 9)
    print(f'Utworzony punkt: {a}')
    a.move(-2, 6)
    print(f'Przesuniety punkt: {a}')
    print(f'Wspolrzedna x: {a.x}, wspolrzedna y: {a.y}')
    print(a.__dict__)
    b: Point = Point(1,1)
    c: NamedPoint = NamedPoint(2,3,'Punkt C')
    print(f' punkt a: {a}')
    print(f' {c}')
    print("zadanie1: ",Point.distance(a,b))


if __name__ == "__main__":
    main()
