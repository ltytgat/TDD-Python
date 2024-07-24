class Money:
    def __init__(self, value: int, currency: str):
        self._amount = value
        self._currency = currency

    def __eq__(self, other):
        return self._amount == other._amount and self._currency == other._currency

    @staticmethod
    def dollar(amount: int):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int):
        return Franc(amount, "CHF")

    def currency(self):
        return self._currency

    def times(self, multiplier: int):
        return Money(self._amount * multiplier, self._currency)


class Dollar(Money):
    def __init__(self, value: int, cur: str):
        super().__init__(value, cur)


class Franc(Money):
    def __init__(self, value: int, cur: str):
        super().__init__(value, cur)
