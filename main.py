class Money:
    def __init__(self, value: int, currency: str):
        self._amount = value
        self._currency = currency

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self._amount == other._amount
        return False

    @staticmethod
    def dollar(amount: int):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int):
        return Franc(amount, "CHF")

    def currency(self):
        return self._currency


class Dollar(Money):
    def __init__(self, value: int, cur: str):
        super().__init__(value, cur)

    def times(self, multiplier: int):
        return Money.dollar(self._amount * multiplier)


class Franc(Money):
    def __init__(self, value: int, cur: str):
        super().__init__(value, cur)

    def times(self, multiplier: int):
        return Money.franc(self._amount * multiplier)
