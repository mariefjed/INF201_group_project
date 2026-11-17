class Temperature:
    """Represents a temperature in Celsius ('C'), Fahrenheit ('F'), or Kelvin ('K')."""

    _TOLERANCE = 1e-9

    def __init__(self, value: float, unit: str = "C") -> None:
        if not isinstance(unit, str) or unit.upper() not in ("C", "F", "K"):
            raise ValueError(f"Invalid temperature unit: {unit!r}. Must be 'C', 'F', or 'K'.")
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Temperature value must be a number.")

        unit_upper = unit.upper()
        val_float = float(value)

        if unit_upper == "C" and val_float < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
        if unit_upper == "F" and val_float < -459.67:
            raise ValueError("Temperature cannot be below absolute zero (-459.67°F).")
        if unit_upper == "K" and val_float < 0.0:
            raise ValueError("Temperature cannot be below absolute zero (0.0 K).")

        self._value = val_float
        self._unit = unit_upper

    @property
    def value(self) -> float:
        return self._value

    @property
    def unit(self) -> str:
        return self._unit

    def _to_kelvin(self) -> float:
        if self._unit == "K":
            return self._value
        if self._unit == "C":
            return self._value + 273.15
        return (self._value - 32.0) * 5.0 / 9.0 + 273.15

    def convert_to(self, target_unit: str) -> "Temperature":
        if not isinstance(target_unit, str) or target_unit.upper() not in ("C", "F", "K"):
            raise ValueError(f"Invalid target unit: {target_unit!r}. Must be 'C', 'F', or 'K'.")

        target = target_unit.upper()
        if target == self._unit:
            return Temperature(self._value, self._unit)

        kelvin = self._to_kelvin()
        if target == "K":
            return Temperature(max(0.0, kelvin), "K")
        if target == "C":
            return Temperature(max(-273.15, kelvin - 273.15), "C")
        return Temperature(max(-459.67, (kelvin - 273.15) * 9.0 / 5.0 + 32.0), "F")

    def __repr__(self) -> str:
        return f"Temperature({self._value}, {self._unit!r})"

    def __str__(self) -> str:
        return f"{self._value:.2f}°{self._unit}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return abs(self._to_kelvin() - other._to_kelvin()) <= self._TOLERANCE

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return not (self == other)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self._to_kelvin() < other._to_kelvin()) and not (self == other)

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self._to_kelvin() < other._to_kelvin()) or (self == other)

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self._to_kelvin() > other._to_kelvin()) and not (self == other)

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self._to_kelvin() > other._to_kelvin()) or (self == other)