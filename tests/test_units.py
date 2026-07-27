from physics_toolkit.units import celsius_to_kelvin


def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == 273.15
    