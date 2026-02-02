import requests

def url_construction(base_url = "https://wttr.in/,", location = "New York", format_type = "j2"):
    """
    Constructs a URL for fetching weather data.

    Parameters:
    - base_url (str): The base URL for the weather service.
    - location (str): The location for which to fetch the weather.
    - format_type (str): The format type for the weather data.

    Returns:
    - str: The constructed URL.
    """
    return f"{base_url}{location}?format={format_type}"


##req = requests.get(url_construction(location = "Tampico,Tamaulipas")) PRUEBA
##print(req.text)