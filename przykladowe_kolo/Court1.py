from datetime import date


class Court:
    __width: float
    __length: float
    __address: str
    __year_built: int

    def __init__(self, width: float = 68, length: float = 150, address: str = '', year_built: int = 0) -> None:
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

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, value: float) -> None:
        self.__width = value

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, value: float) -> None:
        self.__length = value

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str) -> None:
        self.__address = value

    @property
    def year_built(self) -> int:
        return self.__year_built

    @year_built.setter
    def year_built(self, value: int) -> None:
        self.__year_built = value

    def area(self) -> float:
        return self.width * self.length

    @staticmethod
    def validate(obj: 'Court') -> None:
        current_year = date.today().year
        if obj.year_built < 0 or obj.year_built > current_year:
            obj.year_built = current_year

    def __repr__(self) -> str:
        return f'Boisko wybudowane w roku {self.year_built}, ' \
               f'o długości {self.length} i szerokości {self.width}\n' \
               f'Pole powierzchni: {self.area()} mkw.\n' \
               f'Adres: {self.address}\n'

    def __eq__(self, other: 'Court') -> bool:
        if self.area() == other.area():
            return True
        return False

    def __ne__(self, other: 'Court') -> bool:
        if self.area() != other.area():
            return True
        return False
