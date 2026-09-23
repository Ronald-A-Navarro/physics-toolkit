"""
Unit conversion utilities.
"""

# Temperature

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

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert a temperature from Fahrenheit to Celsius.

    Parameters
    ----------
    celsius : float
        Temperature in degrees Fahrenheit.

    Returns
    -------
    float
        Temperature in degrees Celsius.
    """
    return (
        (fahrenheit - FAHRENHEIT_OFFSET)
        / CELSIUS_TO_FAHRENHEIT_SCALE
    )

def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """
    Convert a temperature from Fahrenheit to Kelvin.

    Parameters
    ----------
    fahrenheit : float
        Temperature in degrees Fahrenheit.

    Returns
    -------
    float
        Temperature in Kelvin.
    """
    return celsius_to_kelvin(
        fahrenheit_to_celsius(fahrenheit)
    )

def kelvin_to_fahrenheit(kelvin: float) -> float:
    """
    Convert a temperature from Kelvin to Fahrenheit.
    
    Parameters
    ----------
    Kelvin : float
        Temperature in Kelvin.
    
    Returns
    -------
    float
        Temperature in degrees Fahrenheit.
    """
    return celsius_to_fahrenheit(
        kelvin_to_celsius(kelvin)
    )

# Length

MILES_TO_KILOMETERS = 1.609344

CENTIMETERS_PER_INCH = 2.54

METERS_PER_FOOT = 0.3048

def meters_to_kilometers(meters: float) -> float:
    """
    Convert a length from meters to kilometers.

    Parameters
    ----------
    meters: float
        Length in meters.
    
    Returns
    -------
    float
        Length in Kilometers.
    """
    return meters / 1000

def kilometers_to_meters (kilometers: float) -> float:
    """
    Convert a length from kilometers to meters.

    Parameters
    ----------
    kilometers: float
        Length in kilometers.
    
    Returns
    -------
    float
        Length in meters.
    """
    return kilometers * 1000

def miles_to_kilometers(miles: float) -> float:
    """
    Convert a length from miles to kilometers.
    
    Parameters
    ----------
    miles: float
        Length in miles.
        
    Returns
    -------
    float
        Length in kilometers.
    """
    return miles * MILES_TO_KILOMETERS

def kilometers_to_miles (kilometers: float) -> float:
    """
    Convert a length from kilometers to miles.
        
    Parameters
    ----------
    kilometers: float
        Length in kilometers.
            
    Returns
    -------
    float
        Length in miles.
    """
    return kilometers / MILES_TO_KILOMETERS

def centimeters_to_inches(centimeters: float) -> float:
    """
     Convert a length from centimeters to inches.
            
    Parameters
    ----------
    centimeters: float
        Length in centimeters.
                
    Returns
    -------
    float
        Length in inches.
    """

    return centimeters / CENTIMETERS_PER_INCH

def inches_to_centimeters(inches: float) -> float:
    """
    Convert a length from inches to centimeters.

    Parameters
    ----------
    inches : float
        Length in inches.

    Returns
    -------
    float
        Length in centimeters.
    """
    return inches * CENTIMETERS_PER_INCH

def centimeters_to_meters(centimeters: float) -> float:
    """
    Convert a length from centimeters to meters.

    Parameters
    ----------
    centimeters : float
        Length in centimeters.

    Returns
    -------
    float
        Length in meters.
    """
    return centimeters / 100

def meters_to_centimeters(meters: float) -> float:
    """
    Convert a length from meters to centimeters.
    
    Parameters
    ----------
    meters : float
        Length in meters.
    
    Returns
    -------
    float
        Length in centimeters.
    """
    return meters * 100


def feet_to_meters(feet: float) -> float:
    """
    Convert a length from feet to meters.
        
    Parameters
    ----------
    feet : float
        Length in feet.
        
    Returns
    -------
    float
        Length in meters.
    """
    return feet * METERS_PER_FOOT

def meters_to_feet(meters: float) -> float:
    """
    Convert a length from meters to feet.
            
    Parameters
    ----------
    meters : float
        Length in meters.
            
    Returns
    -------
    float
        Length in feet.
    """
    return meters / METERS_PER_FOOT

# Mass

KILOGRAMS_PER_POUND = 0.45359237

def kilograms_to_grams(kilograms: float) -> float:
    """
    Convert mass from kilograms to grams.
                
    Parameters
    ----------
    kilograms : float
        mass in kilograms.
                
    Returns
    -------
    float
        mass in grams.
    """
    return kilograms * 1000

def grams_to_kilograms(grams: float) -> float:
    """
    Convert mass from grams to kilograms.
                
    Parameters
    ----------
    grams : float
        mass in grams.
                
    Returns
    -------
    float
        mass in kilograms.
    """
    return grams / 1000

def kilograms_to_pounds(kilograms: float) -> float:
    """
    Convert mass from kilograms to pounds.

    Parameters
    ----------
    kilograms : float
        mass in kilograms.

    Returns
    -------
    float
        mass in pounds.
    """
    return kilograms / KILOGRAMS_PER_POUND

def pounds_to_kilograms(pounds: float) -> float:
    """
    Convert mass from pounds to kilograms.

    Parameters
    ----------
    pounds : float
        mass in pounds.

    Returns
    -------
    float
        mass in kilograms.
    """
    return pounds * KILOGRAMS_PER_POUND

# Time

def hours_to_seconds(hours: float) -> float:
    """
    Convert time from hours to seconds.

    Parameters
    ----------
    hours : float
        time in hours.

    Returns
    -------
    float
        time in seconds.
    """
    return hours * 3600