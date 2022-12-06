import sys
import math
from typing import List


class Pizza:
    __price: float
    __toppings: List[str]
    __diameter: float

    def __init__(self, diameter: float, toppings: List[str]):
        if diameter < 20:
            print("Błędna średnica")
            sys.exit(-10)
        else:
            self.__diameter = diameter

        self.__toppings = toppings
        self.__price = round((0.005 * self.area(self)) + len(self.__toppings) * 2, 2)


    @staticmethod
    def area(klasa: 'Pizza'):
        return math.pi * (klasa.__diameter/2)**2

    @property
    def diamater(self):
        return self.__diameter

    @diamater.setter
    def diamater(self, diamater: float):
        if diamater < 20:
            print("Błędna średnica")
            sys.exit(-10)
        else:
            self.__diameter = diamater
            self.__price = (0.005 * self.area(self)) + len(self.__toppings) * 2

    @property
    def price(self):
        return self.__price

    @property
    def toppings(self):
        return self.__toppings

    def add_topping(self, topping: str):
        self.__toppings.append(topping)
        self.__price += 2.0

    def __str__(self):
        if len(self.__toppings) == 0:
            return f'Pizza:\n' \
                   f'średnica: {self.diamater}\n' \
                   f'cena: {self.__price}\n'

        return f'Pizza:\n' \
               f'średnica: {self.diamater}\n' \
               f'dodatki: {self.__toppings}\n' \
               f'cena: {self.__price}\n'

    def __add__(self, other: 'Pizza'):
        srednica = other.diamater
        if self.diamater > other.diamater:
            srednica = self.diamater
        list3 = []
        list3.extend(self.__toppings)
        list3.extend(other.__toppings)
        return Pizza(srednica, list3)
