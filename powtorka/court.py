from datetime import date


class Court:
    __width: float
    __length: float
    __address: str
    __year_built: int

    def __init__(self, width: float = 68, length: float = 150,
                 address: str = '', year_built: int = 0):

        if year_built < 2008 and (length < 90 or length > 120 or width < 45 or width > 90):
            self.__width = 68
            self.__length = 150
        else:
            self.__width = width
            self.__length = length

        self.__address = address
        self.__year_built = year_built

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: float):
        if width < 45 or width > 90:
            raise ValueError("Wprowadzona szerokosc nie znajduje sie w przedziale")

        self.__width = width

    @width.getter
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: float):
        if length < 90 or length > 120:
            raise ValueError("Wprowadzona dlugosc nie znajduje sie w przedziale")

        self.__length = length

    @length.getter
    def length(self):
        return self.__length

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        if type(address) != str:
            raise ValueError("Wprowadzony zly typ adresu")

        self.__address = address

    @address.getter
    def address(self):
        return self.__address

    @property
    def year_built(self):
        return self.__year_built

    @year_built.setter
    def year_built(self, year_built: int):
        if type(year_built) != int:
            raise ValueError("Wprowadzony zly typ roku zbudowania")

        self.__year_built = year_built

    @year_built.getter
    def year_built(self):
        return self.__year_built

    def area(self):
        return self.width * self.length

    @staticmethod
    def validate(klasa: 'Court'):
        curr = date.today().year
        if klasa.year_built > curr or klasa.year_built < 0:
            klasa.year_built = curr

    def __str__(self):
        return f'Boisko wybudowane w roku {self.year_built}, o długości {self.length} metrów ' \
               f'i szerokości {self.width} metrów.\n' \
               f'Pole powierzchni: {self.area()} mkw.\n' \
               f'Adres: {self.address}.\n'

    def __eq__(self, __klasa2: 'Court'):
        return self.area() == __klasa2.area()

    def __ne__(self, __klasa2: 'Court'):
        return self.area() != __klasa2.area()
