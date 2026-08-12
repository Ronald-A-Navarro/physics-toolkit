import pytest

from physics_toolkit.units import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_celsius,
    kelvin_to_fahrenheit,
    kilometers_to_meters,
    meters_to_kilometers,
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
    
def test_fahrenheit_to_celsius_freezing_point():
    assert fahrenheit_to_celsius(32) == 0


def test_fahrenheit_to_celsius_boiling_point():
    assert fahrenheit_to_celsius(212) == 100


def test_fahrenheit_to_celsius_equal_scales():
    assert fahrenheit_to_celsius(-40) == -40


def test_fahrenheit_to_celsius_absolute_zero():
    assert  fahrenheit_to_celsius(-459.67) == pytest.approx(-273.15)


def test_fahrenheit_to_kelvin_freezing_point():
    assert fahrenheit_to_kelvin(32) == 273.15


def test_fahrenheit_to_kelvin_boiling_point():
    assert fahrenheit_to_kelvin(212) == 373.15


def test_fahrenheit_to_kelvin_absolute_zero():
    assert fahrenheit_to_kelvin(-459.67) == 0

def test_kelvin_to_fahrenheit_absolute_zero():
    assert kelvin_to_fahrenheit(0) == pytest.approx(-459.67)


def test_kelvin_to_fahrenheit_freezing_point():
    assert kelvin_to_fahrenheit(273.15) == 32


def test_kelvin_to_fahrenheit_boiling_point():
    assert kelvin_to_fahrenheit(373.15) == 212


def test_meters_to_kilometers_zero():
    assert meters_to_kilometers(0) == 0


def test_meters_to_kilometers_one_kilometer():
    assert meters_to_kilometers(1000) == 1


def test_meters_to_kilometers_fractional():
    assert meters_to_kilometers(2500) == 2.5


def test_meters_to_kilometers_marathon():
    assert meters_to_kilometers(42195) == 42.195
    

def test_kilometers_to_meters_zero():
    assert kilometers_to_meters(0) == 0


def test_kilometers_to_meters_one():
    assert kilometers_to_meters(1) == 1000


def test_kilometers_to_meters_decimal():
    assert kilometers_to_meters(2.5) == 2500


def test_kilometers_to_meters_marathon():
    assert kilometers_to_meters(42.195) == 42195