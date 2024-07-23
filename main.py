class Money:
    def __init__(self, value: int):
        self._amount = value

    def __eq__(self, other):
        if isinstance(other, Money):
            return self._amount == other._amount
        return False


class Dollar(Money):
    def times(self, multiplier: int):
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier: int):
        return Franc(self._amount * multiplier)
