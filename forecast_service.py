import requests


class ForecastService:
    """
    forecast_controller class

    Attributes
    ----------
    apikey : string
        apikey for AccuWeather\
    """

    def __init__(self, apikey):
        self.apikey = apikey

    def get_location_key(self, location):
        """
        get_location_key function

        Parameters
        ----------
        location : string
            location for AccuWeather

        Returns
        -------
        string
            location_key for AccuWeather
        """
        url = (
            "http://dataservice.accuweather.com/locations/v1/cities/search?apikey="
            + self.apikey
            + "&q="
            + location
        )

        try:
            response = requests.get(url)
            print(f"Request URL: {url}")
            print(f"Response status code: {response.status_code}")
            response.raise_for_status()
            return response.json()[0]["Key"]
        except requests.exceptions.RequestException as e:
            message = f"Error fetching location key: {e}"
            print(message)
            raise Exception(message)
        except IndexError as e:
            message = f"Error fetching location key: {e}"
            print(message)
            raise Exception(message)

    def get_current_weather(self, location_key):
        """
        get_current_weather function

        Parameters
        ----------
        location_key : string
            location_key for AccuWeather

        Returns
        -------
        dict
            dictionary of current weather data
        """
        url = (
            "http://dataservice.accuweather.com/currentconditions/v1/"
            + location_key
            + "?apikey="
            + self.apikey
            + "&details=true"
        )
        try:
            response = requests.get(url)
            response.raise_for_status()
            # print(response.json())
            return response.json()
        except requests.exceptions.RequestException as e:
            message = f"Error fetching current weather: {e}"
            print(message)
            raise Exception(message)
