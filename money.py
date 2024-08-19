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

    def reduce(self, bank, to):
        rate = bank.rate(self._currency, to)
        return Money(int(self._amount / rate), to)


class Summ:
    def __init__(self, augend: Money, addend: Money):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to: str):
        amount = self.augend.reduce(bank, to)._amount + self.addend.reduce(bank, to)._amount
        return Money(amount, to)

    def plus(self, addend):
        return Summ(self, addend)

    def times(self, multi):
        return Summ(self.augend.times(multi), self.addend.times(multi))


class Bank:
    def __init__(self):
        self.rates = {}

    def reduce(self, source, to):
        return source.reduce(self, to)

    def rate(self, origin, to):
        if origin == to:
            return 1
        pair = Pair(origin, to)
        rate = self.rates[str(pair)]
        return int(rate)

    def add_rate(self, origin, to, rate):
        self.rates[str(Pair(origin, to))] = rate


class Pair:
    def __init__(self, origin, to):
        self.origin = origin
        self.to = to

    def __eq__(self, other):
        return self.origin == other.origin and self.to == other.to

    def __str__(self):
        return f"{self.origin}-{self.to}"
