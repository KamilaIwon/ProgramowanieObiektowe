from Court1 import Court
from typing import Optional


class Stadium(Court):
    __name: str
    __common_name: Optional[str]
    __capacity: int

    def __init__(self, width: float = 68, length: float = 150, address: str = '',
                 year_built: int = 0, name: str = '', common_name: Optional[str] = '',
                 capacity: int = 0) -> None:
        super().__init__(width, length, address, year_built)
        self.__name = name
        self.__common_name = common_name
        if capacity >= 0:
            self.__capacity = capacity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def common_name(self) -> str:
        return self.__common_name

    @common_name.setter
    def common_name(self, value: str) -> None:
        self.common_name = value

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        if value < 0:
            print(f'niepoprawne dane')
        self.__capacity = value

    def __eq__(self, other: 'Stadium') -> bool:
        if self.area() == other.area() and self.capacity == other.capacity:
            return True
        return False

    def __ne__(self, other: 'Stadium') -> bool:
        if self.area() != other.area() or self.capacity != other.capacity:
            return True
        return False

    def __repr__(self) -> str:
        text = f"Boisko wybudowane w {self.year_built}, " \
               f"o długości {self.length} i szerokości {self.width} metrów.\n" \
               f"Pole powierzchni: {self.area()} mkw.\n" \
               f"Adres: {self.address}.\n" \
               f"Nazwa: {self.name}.\n"
        if self.common_name is not None and self.common_name != '':
            text += f"Nazwa zwyczajowa: {self.common_name}.\n"
        text += f"Pojemność stadionu {self.capacity}.\n"
        return text
