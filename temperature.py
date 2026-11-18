
class Temperature:
    tolerance = 1e-9

    def __init__(self, value: float, unit: str):
        """Initiates the class with a temperature value and unit"""
        if not isinstance(unit, str):
            raise ValueError("Unit must be a string")

        u = unit.upper()
        if u not in ("C", "K", "F"):
            raise ValueError(f"{unit} must be C, K, or F")

        if not isinstance(value, float | int):
            raise ValueError("Value must be a float or int")

        if u == "C":
            k_val = value + 273.15
        elif u == "F":
            k_val = (value - 32) * 5 / 9 + 273.15
        else:
            k_val = float(value)

        if k_val <- self.tolerance:
            raise ValueError("Temperature can not be below absolute zero (0 K)")

        self._value = float(value)
        self._unit = u

    @property
    def value(self) -> float:
        """Expose value as a read-only attribute"""
        return self._value

    @property
    def unit(self) -> str:
        """Expose unit as a read-only attribute"""
        return self._unit

    def to_celsius(self) -> float:
        """Converts temperature to celsius"""
        if self._unit == "C":
            C = self._value 

        if self._unit == "K":
            C = self._value - 273.15 

        if self._unit == "F":
            C = (self._value - 32)*(5/9)
        return C

    def to_fahrenheit(self) -> float:
        """Converts temperature to Fahrenheit"""
        if self._unit == "F":
            F = self._value 

        if self._unit == "C":
            F = (self._value * 9/5) + 32

        if self._unit == "K":
            F = (self._value - 273.15) * 9/5 + 32
        return F

    def to_kelvin(self) -> float:
        """Converts temperature to Kelvin"""
        if self._unit == "K":
            K = self._value 

        if self._unit == "C":
            K = self._value + 273.15

        if self._unit == "F":
            K = (self._value - 32) * 5/9 + 273.15
        return K

    def convert_to(self, target_unit: str) -> Temperature:
        """Converts any temperature to target unit"""
        if not isinstance(target_unit, str):
            raise ValueError("Target unit must be a string")

        tu = target_unit.upper()
        if tu not in ("F", "K", "C"):
            raise ValueError(f"Target unit ({target_unit}) must be C, K or F")
        
        if tu == "C":
            if self._unit == "C":
                new_temp = self._value 

            if self._unit == "F" or "K":
                new_temp = self.to_celsius()

        if tu == "K":
            if self._unit == "K":
                new_temp = self._value 
        
            if self._unit == "F" or "C":
                new_temp = self.to_kelvin()

        if tu == "F":
            if self._unit == "F":
                new_temp = self._value 
        
            if self._unit == "C" or "K":
                new_temp = self.to_fahrenheit()

        return Temperature(new_temp, tu)

    def __repr__(self) -> str:
        return f"Temperature({self._value}, '{self._unit}')"

    def __str__(self) -> str:
        if self._unit == "K":
            return f"{self._value:.2f} {self._unit}"
        else:
            return f"{self._value:.2f} °{self._unit}"

    def __eq__(self, other):
        """Checks if two temperatures are equal (==)"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return abs(self.to_kelvin() - other.to_kelvin()) <= self.tolerance

    def __ne__(self, other):
        """Checks if two temperatures are not equal (!=)"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return not (self == other)

    def __lt__(self, other):
        """Checks if temperature is below other (<)"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_kelvin() < other.to_kelvin() - self.tolerance

    def __le__(self, other):
        """Checks if temp is equal or below other (<=)"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_kelvin() <= other.to_kelvin() + self.tolerance

    def __gt__(self, other):
        """Checks if temp is larger than other (>)"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_kelvin() > other.to_kelvin() + self.tolerance

    def __ge__(self, other):
        """Checks if temp is larger or equal to other (>=)"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_kelvin() >= other.to_kelvin() - self.tolerance