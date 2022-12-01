
class Court:
    __width: float
    __length: float
    __address: str
    __year_built: int

    def __init__(self, address: str, year_built: int, width: float = 68, length: float = 150) -> None:
        if year_built < 2008:
            if 45 <= width <= 90 and 90 <= length <= 120:
                self.__width = width
                self.__length = length
            else:
                self.__width = 68
                self.__length = 150
        else:
            self.__width = width
            self.__length = length
        self.__address = address
        self.__year_built = year_built

    def __str__(self) -> str:
        return f'width: {self.__width}\n' \
               f'length: {self.__length}\n' \
               f'address: {self.__address}\n' \
               f'year built: {self.__year_built}'

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, value: float) -> None:
        self.__width = value

    def area(self) -> float:
        return self.__width * self.__length


zmienna1 = Court('lotnicza', 2009, 190, 200)
zmienna2 = Court('apparel', 2014, 70, 115)

print(zmienna1)
