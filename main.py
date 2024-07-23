class Money:
    def __init__(self, value: int):
        self._amount = value

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self._amount == other._amount
        return False


class Dollar(Money):
    def times(self, multiplier: int):
        return Money(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier: int):
        return Money(self._amount * multiplier)
