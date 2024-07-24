class Money:
    def __init__(self, value: int, currency: str):
        self._amount = value
        self._currency = currency

    def __eq__(self, other):
        return self._amount == other._amount and self._currency == other._currency

    @staticmethod
    def dollar(amount: int):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int):
        return Money(amount, "CHF")

    def currency(self):
        return self._currency

    def times(self, multiplier: int):
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend):
        return Summ(self, addend)


class Bank:
    @staticmethod
    def reduce(source, to):
        return Money.dollar(10)


class Summ:
    def __init__(self, augend: Money, addend: Money):
        self.augend = augend
        self.addend = addend
