"""
Unit conversion utilities.
"""

CELSIUS_TO_KELVIN_OFFSET = 273.15


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
