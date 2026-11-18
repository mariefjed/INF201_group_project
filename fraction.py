import math


class Fraction:
    """Represents a reduced rational number with a strictly positive integer denominator."""

    def __init__(self, numerator: int, denominator: int = 1) -> None:
        if isinstance(numerator, bool) or not isinstance(numerator, int):
            raise TypeError("Numerator must be an integer.")
        if isinstance(denominator, bool) or not isinstance(denominator, int):
            raise TypeError("Denominator must be an integer.")
        if denominator <= 0:
            raise ValueError("Denominator must be a positive integer (> 0).")

        common = math.gcd(abs(numerator), denominator)
        self._numerator = numerator // common
        self._denominator = denominator // common

    @property
    def numerator(self) -> int:
        return self._numerator

    @property
    def denominator(self) -> int:
        return self._denominator

    def __repr__(self) -> str:
        return f"Fraction({self._numerator}, {self._denominator})"

    def __str__(self) -> str:
        return f"{self._numerator}/{self._denominator}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return (
            self._numerator == other._numerator
            and self._denominator == other._denominator
        )

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return not (self == other)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._numerator * other._denominator < other._numerator * self._denominator

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._numerator * other._denominator <= other._numerator * self._denominator

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._numerator * other._denominator > other._numerator * self._denominator

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._numerator * other._denominator >= other._numerator * self._denominator

    def __add__(self, other: object) -> "Fraction":
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self._numerator * other._denominator + other._numerator * self._denominator
        den = self._denominator * other._denominator
        return Fraction(num, den)

    def __sub__(self, other: object) -> "Fraction":
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self._numerator * other._denominator - other._numerator * self._denominator
        den = self._denominator * other._denominator
        return Fraction(num, den)

    def __mul__(self, other: object) -> "Fraction":
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(
            self._numerator * other._numerator,
            self._denominator * other._denominator,
        )

    def __truediv__(self, other: object) -> "Fraction":
        if not isinstance(other, Fraction):
            return NotImplemented
        if other._numerator == 0:
            raise ZeroDivisionError("Cannot divide by a zero fraction.")
        num = self._numerator * other._denominator
        den = self._denominator * other._numerator
        if den < 0:
            num = -num
            den = -den
        return Fraction(num, den)

    def __neg__(self) -> "Fraction":
        return Fraction(-self._numerator, self._denominator)

    def __abs__(self) -> "Fraction":
        return Fraction(abs(self._numerator), self._denominator)

    def __float__(self) -> float:
        return self._numerator / self._denominator