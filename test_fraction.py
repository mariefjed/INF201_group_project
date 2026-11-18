import pytest

from fraction import Fraction


def test_initialization_and_reduction():
    f1 = Fraction(2, 4)
    assert f1.numerator == 1
    assert f1.denominator == 2

    f2 = Fraction(-6, 9)
    assert f2.numerator == -2
    assert f2.denominator == 3

    f3 = Fraction(0, 5)
    assert f3.numerator == 0
    assert f3.denominator == 1


def test_read_only_attributes():
    f = Fraction(3, 4)
    with pytest.raises(AttributeError):
        f.numerator = 5  # type: ignore
    with pytest.raises(AttributeError):
        f.denominator = 8  # type: ignore


@pytest.mark.parametrize("bad_den", [0, -1, -10])
def test_non_positive_denominator_raises_value_error(bad_den):
    with pytest.raises(ValueError):
        Fraction(1, bad_den)


@pytest.mark.parametrize(
    "num, den",
    [
        (1.5, 2),
        (1, 2.5),
        (1, "2"),
        ("1", 2),
        (True, 2),
        (1, False),
    ],
)
def test_non_integer_arguments_raise_type_error(num, den):
    with pytest.raises(TypeError):
        Fraction(num, den)


def test_equality_and_inequality():
    assert Fraction(1, 2) == Fraction(2, 4)
    assert Fraction(1, 2) != Fraction(1, 3)


def test_ordering():
    f_small = Fraction(1, 3)
    f_large = Fraction(1, 2)

    assert f_small < f_large
    assert f_small <= f_large
    assert f_small <= Fraction(2, 6)
    assert f_large > f_small
    assert f_large >= f_small
    assert f_large >= Fraction(3, 6)


def test_comparison_with_non_fraction():
    f = Fraction(1, 2)
    assert (f == 0.5) is False
    assert (f != 0.5) is True
    with pytest.raises(TypeError):
        _ = f < 0.5


def test_str_and_repr():
    f = Fraction(2, 4)
    assert str(f) == "1/2"
    assert repr(f) == "Fraction(1, 2)"


def test_arithmetic_operations():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)

    assert f1 + f2 == Fraction(5, 6)
    assert f1 - f2 == Fraction(1, 6)
    assert f1 * f2 == Fraction(1, 6)
    assert f1 / f2 == Fraction(3, 2)
    assert f1 / Fraction(-1, 3) == Fraction(-3, 2)


def test_division_by_zero_fraction():
    with pytest.raises(ZeroDivisionError):
        _ = Fraction(1, 2) / Fraction(0, 1)


def test_unary_and_float_conversions():
    f = Fraction(-3, 4)
    assert -f == Fraction(3, 4)
    assert abs(f) == Fraction(3, 4)
    assert float(Fraction(1, 4)) == pytest.approx(0.25)