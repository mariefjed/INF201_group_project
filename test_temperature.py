import pytest

from temperature import Temperature


def test_initialization_default_and_case_insensitive():
    t_default = Temperature(25)
    assert t_default.value == 25.0
    assert t_default.unit == "C"

    t_lower = Temperature(300, "k")
    assert t_lower.value == 300.0
    assert t_lower.unit == "K"


def test_read_only_attributes():
    t = Temperature(20, "C")
    with pytest.raises(AttributeError):
        t.value = 30  # type: ignore
    with pytest.raises(AttributeError):
        t.unit = "F"  # type: ignore


@pytest.mark.parametrize("bad_unit", ["X", "Celsius", "Fahrenheit", "Kelvin", "", "°C"])
def test_invalid_unit_raises_value_error(bad_unit):
    with pytest.raises(ValueError):
        Temperature(10, bad_unit)


def test_invalid_target_unit_in_convert_to():
    t = Temperature(10, "C")
    with pytest.raises(ValueError):
        t.convert_to("Rankine")


@pytest.mark.parametrize(
    "value, unit",
    [
        (-273.16, "C"),
        (-459.68, "F"),
        (-0.01, "K"),
    ],
)
def test_below_absolute_zero_raises_value_error(value, unit):
    with pytest.raises(ValueError):
        Temperature(value, unit)


@pytest.mark.parametrize(
    "celsius, fahrenheit, kelvin",
    [
        (-273.15, -459.67, 0.0),
        (-40.0, -40.0, 233.15),
        (0.0, 32.0, 273.15),
        (37.0, 98.6, 310.15),
        (100.0, 212.0, 373.15),
    ],
)
def test_reference_point_conversions(celsius, fahrenheit, kelvin):
    t_c = Temperature(celsius, "C")
    t_f = Temperature(fahrenheit, "F")
    t_k = Temperature(kelvin, "K")

    assert t_c.convert_to("F").value == pytest.approx(fahrenheit, abs=1e-9)
    assert t_c.convert_to("K").value == pytest.approx(kelvin, abs=1e-9)
    assert t_f.convert_to("C").value == pytest.approx(celsius, abs=1e-9)
    assert t_k.convert_to("C").value == pytest.approx(celsius, abs=1e-9)

    assert t_c == t_f
    assert t_c == t_k
    assert t_f == t_k


def test_convert_to_returns_new_instance():
    t1 = Temperature(25, "C")
    t2 = t1.convert_to("C")
    t3 = t1.convert_to("F")

    assert t2 is not t1
    assert t3 is not t1
    assert t1.unit == "C"
    assert t1.value == 25.0


def test_ordering_and_tolerance():
    t_cold = Temperature(0, "C")
    t_warm = Temperature(100, "F")
    t_almost_cold = Temperature(273.15 + 5e-10, "K")

    assert t_cold < t_warm
    assert t_cold <= t_warm
    assert t_warm > t_cold
    assert t_warm >= t_cold
    assert t_cold != t_warm
    assert t_cold == t_almost_cold


def test_comparison_with_non_temperature():
    t = Temperature(20, "C")
    assert (t == 20) is False
    assert (t != 20) is True
    with pytest.raises(TypeError):
        _ = t < 20


def test_str_and_repr():
    t = Temperature(37, "C")
    assert str(t) == "37.00°C"
    assert repr(t) == "Temperature(37.0, 'C')"
