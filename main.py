class Money:
    def __init__(self, value: int):
        self._amount = value
        self._currency = ""

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self._amount == other._amount
        return False

    @staticmethod
    def dollar(amount: int):
        return Dollar(amount)

    @staticmethod
    def franc(amount: int):
        return Franc(amount)

    def currency(self):
        return self._currency


class Dollar(Money):
    def __init__(self, value: int, cur: str):
        super().__init__(value)
        self._currency = "USD"

    def times(self, multiplier: int):
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def __init__(self, value: int):
        super().__init__(value)
        self._currency = "CHF"

    def times(self, multiplier: int):
        return Franc(self._amount * multiplier)
