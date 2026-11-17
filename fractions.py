
class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        """Represents a fraction where denominator have to be a positive integer"""
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Denominator and numerator have to be integers")


        if denominator <= 0:
            raise ValueError("Denominator have to be positive integer")
            

        # Forenkler brøken med største felles divisor (GCD)
        common_divisor = math.gcd(abs(numerator), denominator)
        self._numerator = numerator // common_divisor
        self._denominator = denominator // common_divisor

    @property
    def numerator(self) -> int:
        """Read-only for numerator."""
        return self._numerator

    @property
    def denominator(self) -> int:
        """Read-only for denominator"""
        return self._denominator


