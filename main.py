class Dollar:
    def __init__(self, value: int):
        self.amount = value

    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)

    def equals(self, obj):
        return self.amount == obj.amount
