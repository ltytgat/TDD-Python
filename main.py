class Dollar:
    def __init__(self, value: int):
        self.__amount = value

    def times(self, multiplier: int):
        return Dollar(self.__amount * multiplier)

    def __eq__(self, other):
        if isinstance(other, Dollar):
            return self.__amount == other.__amount
        return False


class Franc:
    def __init__(self, value: int):
        self.__amount = value

    def times(self, multiplier: int):
        return Franc(self.__amount * multiplier)

    def __eq__(self, other):
        if isinstance(other, Franc):
            return self.__amount == other.__amount
        return False
