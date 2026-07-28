"""
Unit conversion utilities.
"""

CELSIUS_TO_KELVIN_OFFSET = 273.15

FAHRENHEIT_OFFSET = 32.0
CELSIUS_TO_FAHRENHEIT_SCALE = 9 / 5


def celsius_to_kelvin(celsius: float) -> float:
    """
    Convert a temperature from Celsius to Kelvin.

    Parameters
    ----------
    celsius : float
        Temperature in degrees Celsius.

    Returns
    -------
    float
        Temperature in Kelvin.
    """
    return celsius + CELSIUS_TO_KELVIN_OFFSET

def kelvin_to_celsius(kelvin: float) -> float:
    """
    Convert a temperature from Kelvin to Celsius.

    Parameters
    ----------
    kelvin : float
        Temperature in Kelvin.

    Returns
    -------
    float
        Temperature in degrees Celsius.
    """
    return kelvin - CELSIUS_TO_KELVIN_OFFSET

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert a temperature from Celsius to Fahrenheit.

    Parameters
    ----------
    celsius : float
        Temperature in degrees Celsius.

    Returns
    -------
    float
        Temperature in degrees Fahrenheit.
    """
    return (
        celsius * CELSIUS_TO_FAHRENHEIT_SCALE 
        + FAHRENHEIT_OFFSET
    )
