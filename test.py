from main import Money, Bank, Summ


def test_multiplication():
    five = Money.dollar(5)
    assert five.times(2) == Money.dollar(10)
    assert five.times(3) == Money.dollar(15)


def test_franc_multiplication():
    five = Money.franc(5)
    assert five.times(2) == Money.franc(10)
    assert five.times(3) == Money.franc(15)


def test_equality():
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(5) != Money.dollar(6)
    assert Money.franc(5) != Money.dollar(5)


def test_currency():
    assert "USD" == Money.dollar(1).currency()
    assert "CHF" == Money.franc(1).currency()


def test_different_class_equality():
    assert Money(10, "CHF") == Money.franc(10)


def test_simple_addition():
    five = Money.dollar(5)
    summ = five.plus(five)
    bank = Bank()
    reduced = bank.reduce(summ, "USD")
    assert Money.dollar(10) == reduced


def test_plus_return_sum():
    five = Money.dollar(5)
    result = five.plus(five)
    summ = result
    assert five == summ.augend
    assert five == summ.addend


def test_reduce_sum():
    summ = Summ(Money.dollar(3), Money.dollar(4))
    bank = Bank()
    result = bank.reduce(summ, "USD")
    assert Money.dollar(7) == result


def test_reduce_money():
    bank = Bank()
    result = bank.reduce(Money.dollar(1), "USD")
    assert Money.dollar(1) == result
