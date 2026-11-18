from temperature2 import Temperature
import pytest



def test_initialization():
    # Tests case-insensitive units
    t1 = Temperature(20, "C")
    t2 = Temperature(20, "c")
    assert t1.unit == "C"
    assert t2.unit == "C"
    assert t1.value == 20

    # Tests read-only behavior - fails if you change the values
    with pytest.raises(AttributeError):
        t1.value = 30.0
    with pytest.raises(AttributeError):
        t1.unit = "F"

def test_validation():
    with pytest.raises(ValueError):
        t1 = Temperature(20, "X")
    with pytest.raises(ValueError):
        t1 = Temperature(20, 4)

    with pytest.raises(ValueError):
        t1 = Temperature(-274, "C")

    with pytest.raises(ValueError):
        t1 = Temperature(-1, "K")

    with pytest.raises(ValueError):
        t1 = Temperature(-460, "F")


def test_conversions():
    # 1. Absolutt nullpunkt (0 K = -273.15 °C = -459.67 °F)
    k = Temperature(0, "K")
    assert pytest.approx(k.to_celsius(), abs=1e-5) == -273.15
    assert pytest.approx(k.to_fahrenheit(), abs=1e-5) == -459.67

    # 2. Celsius-Fahrenheit crossover (-40 °C == -40 °F)
    c_cross = Temperature(-40, "C")
    assert pytest.approx(c_cross.to_fahrenheit(), abs=1e-5) == -40.0

    # 3. Frysepunkt for vann (0 °C = 32 °F = 273.15 K)
    water_freeze = Temperature(0, "C")
    assert water_freeze.to_fahrenheit() == 32.0
    assert pytest.approx(water_freeze.to_kelvin(), abs=1e-5) == 273.15

    # 4. Menneskekroppstemperatur (~37 °C = 98.6 °F = 310.15 K)
    body = Temperature(37, "C")
    assert pytest.approx(body.to_fahrenheit(), abs=1e-5) == 98.6
    assert pytest.approx(body.to_kelvin(), abs=1e-5) == 310.15

    # 5. Kokepunkt for vann (100 °C = 212 °F = 373.15 K)
    water_boil = Temperature(100, "C")
    assert water_boil.to_fahrenheit() == 212.0
    assert pytest.approx(water_boil.to_kelvin(), abs=1e-5) == 373.15

def test_round_trip_conversions():
    # "C" -> "F" -> "K" -> "C"
    original = Temperature(25.0, "C")
    f_temp = original.convert_to("F")
    k_temp = f_temp.convert_to("K")
    final_temp = k_temp.convert_to("C")

    assert final_temp == original
    assert pytest.approx(final_temp.value) == original.value

def test_cross_unit_comparisons():
    # 0 °C == 32 °F == 273.15 K
    c = Temperature(0, "C")
    f = Temperature(32, "F")
    k = Temperature(273.15, "K")

    assert c == f
    assert f == k
    assert c == k

    # Større enn / mindre enn på tvers av enheter
    cold = Temperature(-10, "C") # 263.15 K
    warm = Temperature(50, "F")  # 283.15 K
    assert cold < warm
    assert warm > cold
    assert cold <= warm
    assert warm >= cold
    assert cold != warm

    # Sammenligning med ikke-Temperature-objekter skal returnere NotImplemented (false for ==)
    assert (c == 32) is False
    assert (c != 32) is True

def test_formatting():
    t = Temperature(25.5, "C")
    assert repr(t) == "Temperature(25.5, 'C')"
    assert str(t) == "25.50 °C"

    t_k = Temperature(300, "K")
    assert str(t_k) == "300.00 K"