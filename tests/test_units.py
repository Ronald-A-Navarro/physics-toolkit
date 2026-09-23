import pytest

from physics_toolkit.units import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    centimeters_to_inches,
    centimeters_to_meters,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    feet_to_meters,
    grams_to_kilograms,
    hours_to_seconds,
    inches_to_centimeters,
    kelvin_to_celsius,
    kelvin_to_fahrenheit,
    kilograms_to_grams,
    kilograms_to_pounds,
    kilometers_to_meters,
    kilometers_to_miles,
    meters_to_centimeters,
    meters_to_feet,
    meters_to_kilometers,
    miles_to_kilometers,
    minutes_to_hours,
    pounds_to_kilograms,
    seconds_to_hours,
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


def test_miles_to_kilometers_zero():
    assert miles_to_kilometers(0) == 0


def test_miles_to_kilometers_one():
    assert miles_to_kilometers(1) == pytest.approx(1.609344)


def test_miles_to_kilometers_decimal():
    assert miles_to_kilometers(2.5) == pytest.approx(4.02336)


def test_miles_to_kilometers_marathon():
    assert miles_to_kilometers(26.21875) == pytest.approx(42.195)


def test_kilometers_to_miles_zero():
    assert kilometers_to_miles(0) == 0


def test_kilometers_to_miles_one():
    assert kilometers_to_miles(1.609344) == pytest.approx(1)


def test_kilometers_to_miles_decimal():
    assert kilometers_to_miles(4.02336) == pytest.approx(2.5)


def test_kilometers_to_miles_marathon():
    assert kilometers_to_miles(42.195) == pytest.approx(26.21875)


def test_centimeters_to_inches_zero():
    assert centimeters_to_inches(0) == 0


def test_centimeters_to_inches_one():
    assert centimeters_to_inches(2.54) == pytest.approx(1)


def test_centimeters_to_inches_two():
    assert centimeters_to_inches(5.08) == pytest.approx(2)


def test_centimeters_to_inches_foot():
    assert centimeters_to_inches(30.48) == pytest.approx(12)


def test_inches_to_centimeters_zero():
    assert inches_to_centimeters(0) == 0


def test_inches_to_centimeters_one():
    assert inches_to_centimeters(1) == pytest.approx(2.54)


def test_inches_to_centimeters_two():
    assert inches_to_centimeters(2) == pytest.approx(5.08)


def test_inches_to_centimeters_foot():
    assert inches_to_centimeters(12) == pytest.approx(30.48)


def test_centimeters_to_meters_zero():
    assert centimeters_to_meters(0) == 0


def test_centimeters_to_meters_one():
    assert centimeters_to_meters(1) == 0.01


def test_centimeters_to_meters_hundred():
    assert centimeters_to_meters(100) == 1


def test_centimeters_to_meters_over_hundred():
    assert centimeters_to_meters(345) == 3.45


def test_centimeters_to_meters_below_hundred():
    assert centimeters_to_meters(46) == 0.46


def test_meters_to_centimeters_zero():
    assert meters_to_centimeters(0) == 0


def test_meters_to_centimeters_below_one():
    assert meters_to_centimeters(0.01) == 1


def test_meters_to_centimeters_one():
    assert meters_to_centimeters(1) == 100


def test_meters_to_centimeters_over_one():
    assert meters_to_centimeters(3.45) == 345


def test_meters_to_centimeters_below_one_meter():
    assert meters_to_centimeters(0.46) == 46


def test_feet_to_meters_zero():
    assert feet_to_meters(0) == 0


def test_feet_to_meters_one():
    assert feet_to_meters(1) == pytest.approx(0.3048)


def test_feet_to_meters_two():
    assert feet_to_meters(2) == pytest.approx(0.6096)


def test_feet_to_meters_ten():
    assert feet_to_meters(10) == pytest.approx(3.048)


def test_meters_to_feet_zero():
    assert meters_to_feet(0) == 0


def test_meters_to_feet_one():
    assert meters_to_feet(0.3048) == pytest.approx(1)


def test_meters_to_feet_two():
    assert meters_to_feet(0.6096) == pytest.approx(2)


def test_meters_to_feet_ten():
    assert meters_to_feet(3.048) == pytest.approx(10)


def test_kilograms_to_grams_zero():
    assert kilograms_to_grams(0) == 0


def test_kilograms_to_grams_one():
    assert kilograms_to_grams(1) == 1000


def test_kilograms_to_grams_ten():
    assert kilograms_to_grams(10) == 10000


def test_kilograms_to_grams_below_thousand():
    assert kilograms_to_grams(500) == 500000


def test_kilograms_to_grams_above_thousand():
    assert kilograms_to_grams(1500) == 1500000


def test_grams_to_kilograms_zero():
    assert grams_to_kilograms(0) == 0


def test_grams_to_kilograms_one():
    assert grams_to_kilograms(1000) == 1


def test_grams_to_kilograms_ten():
    assert grams_to_kilograms(10000) == 10


def test_grams_to_kilograms_below_thousand():
    assert grams_to_kilograms(500000) == 500


def test_grams_to_kilograms_above_thousand():
    assert grams_to_kilograms(1500000) == 1500


def test_kilograms_to_pounds_zero():
    assert kilograms_to_pounds(0) == 0


def test_kilograms_to_pounds_one():
    assert kilograms_to_pounds(1) == pytest.approx(2.20462262)


def test_kilograms_to_pounds_ten():
    assert kilograms_to_pounds(10) == pytest.approx(22.0462262)


def test_kilograms_to_pounds_below_hundred():
    assert kilograms_to_pounds(45) == pytest.approx(99.2080179)


def test_kilograms_to_pounds_above_hundred():
    assert kilograms_to_pounds(120) == pytest.approx(264.5547148)


def test_pounds_to_kilograms_zero():
    assert pounds_to_kilograms(0) == 0


def test_pounds_to_kilograms_one():
    assert pounds_to_kilograms(2.20462262) == pytest.approx(1)


def test_pounds_to_kilograms_ten():
    assert pounds_to_kilograms(22.0462262) == pytest.approx(10)


def test_pounds_to_kilograms_below_hundred():
    assert pounds_to_kilograms(99.2080179) == pytest.approx(45)


def test_pounds_to_kilograms_above_hundred():
    assert pounds_to_kilograms(264.5547148) == pytest.approx(120)


def test_hours_to_seconds_zero():
    assert hours_to_seconds(0) == 0


def test_hours_to_seconds_one():
    assert hours_to_seconds(1) == 3600


def test_hours_to_seconds_two():
    assert hours_to_seconds(2) == 7200


def test_hours_to_seconds_ten():
    assert hours_to_seconds(10) == 36000


def test_seconds_to_hours_zero():
    assert seconds_to_hours(0) == 0


def test_seconds_to_hours_one():
    assert seconds_to_hours(3600) == 1


def test_seconds_to_hours_two():
    assert seconds_to_hours(7200) == 2


def test_seconds_to_hours_half():
    assert seconds_to_hours(1800) == 0.5


def test_minutes_to_hours_zero():
    assert minutes_to_hours(0) == 0


def test_minutes_to_hours_one_hour():
    assert minutes_to_hours(60) == 1


def test_minutes_to_hours_two_hours():
    assert minutes_to_hours(120) == 2


def test_minutes_to_hours_half_hour():
    assert minutes_to_hours(30) == 0.5