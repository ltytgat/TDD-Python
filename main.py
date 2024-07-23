class Dollar:
    def __init__(self, value: int):
        self.__amount = value

    def times(self, multiplier: int):
        return Dollar(self.__amount * multiplier)

    def equals(self, obj):
        return self.__amount == obj.__amount
