class Dollar:
    def __init__(self, value: int):
        self.__amount = value

    def times(self, multiplier: int):
        return Dollar(self.__amount * multiplier)

    def __eq__(self, other):
        return self.__amount == other.__amount
