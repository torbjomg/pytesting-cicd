from pytesting_cicd import functions


def test_add_integers():
    assert functions.add(1, 2) == 3
    assert functions.add(0, 0) == 0
    assert functions.add(-1, -1) == -2
    assert functions.add(1, -1) == 0


def test_subtract_integers():
    assert functions.subtract(1, 2) == -1
    assert functions.subtract(0, 0) == 0


def test_subtract_wrong_types():
    try:
        functions.subtract(1, "a")  # type: ignore
    except TypeError as e:
        assert str(e) == "unsupported operand type(s) for -: 'int' and 'str'"
