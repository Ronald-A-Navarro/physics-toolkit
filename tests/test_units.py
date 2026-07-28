import pytest

from physics_toolkit.units import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    kelvin_to_celsius,
)


def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == 273.15

def test_kelvin_to_celsius_absolute_zero():
    assert kelvin_to_celsius(0) == -273.15


def test_kelvin_to_celsius_freezing_point():
    assert kelvin_to_celsius(273.15) == 0


def test_kelvin_to_celsius_boiling_point():
    assert kelvin_to_celsius(373.15) == 100


def test_celsius_to_fahrenheit_freezing_point():
    assert celsius_to_fahrenheit(0) == 32


def test_celsius_to_fahrenheit_boiling_point():
    assert celsius_to_fahrenheit(100) == 212


def test_celsius_to_fahrenheit_equal_scales():
    assert celsius_to_fahrenheit(-40) == -40


def test_celsius_to_fahrenheit_absolute_zero():
    assert celsius_to_fahrenheit(-273.15) == pytest.approx(-459.67)

    
 