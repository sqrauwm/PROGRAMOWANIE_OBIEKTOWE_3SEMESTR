from court import Court


class Stadium(Court):
    __name: str
    __common_name: str
    __capacity: int

    def __init__(self, width: float = 68, length: float = 150, address: str = '',
                 year_built: int = None, name: str = '', common_name: str = None, capacity: int = 0):
        super().__init__(width, length, address, year_built)

        self.__name = name
        self.__common_name = common_name
        if capacity < 0:
            self.__capacity = 0
        else:
            self.__capacity = capacity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if type(name) != str:
            raise ValueError('Zly typ nazwy stadionu')
        self.__name = name

    @name.getter
    def name(self):
        return self.__name

    @property
    def common_name(self):
        return self.__common_name

    @common_name.setter
    def common_name(self, common_name: str):
        if type(common_name) != str:
            raise ValueError('Zly typ potocznej nazwy stadionu')
        self.__common_name = common_name

    @common_name.getter
    def common_name(self):
        return self.__common_name

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        if capacity < 0:
            self.__capacity = 0

        self.__capacity = capacity

    @capacity.getter
    def capacity(self):
        return self.__capacity

    def __eq__(self, __other: 'Stadium'):
        return self.area() == __other.area() and self.capacity == __other.capacity

    def __ne__(self, __other: 'Stadium'):
        return self.area() != __other.area() and self.capacity != __other.capacity

    def __str__(self):
        if self.common_name is None:
            return f'„Boisko wybudowane w roku {self.year_built}, o długości {self.length} metrów ' \
                   f'i szerokości {self.width} metrów.\n' \
                   f'Pole powierzchni: {self.area()} mkw.\n' \
                   f'Adres: {self.address}.\n' \
                   f'Nazwa: {self.name}.\n' \
                   f'Pojemonść stadionu: {self.capacity} osób.\n'

        return f'„Boisko wybudowane w roku {self.year_built}, o długości {self.length} metrów ' \
               f'i szerokości {self.width} metrów.\n' \
               f'Pole powierzchni: {self.area()} mkw.\n' \
               f'Adres: {self.address}.\n' \
               f'Nazwa: {self.name}.\n' \
               f'Nazwa zwyczajowa: {self.common_name}.\n' \
               f'Pojemonść stadionu: {self.capacity} osób.\n'
