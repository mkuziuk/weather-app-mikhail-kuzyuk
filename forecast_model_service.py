class ForecastModelService:

    def check_weather(self, current_weather):
        """
        температура ниже 0°C или выше 35°C,
        скорость ветра выше 50 км/ч,
        вероятность осадков выше 70%
        """
        if not current_weather:
            return "Unable to retrieve current weather"

        try:
            temperature = current_weather[0]["Temperature"]["Metric"]["Value"]
            wind_speed = current_weather[0]["Wind"]["Speed"]["Metric"]["Value"]
            precipitation_probability = current_weather[0]["PrecipitationSummary"][
                "PastHour"
            ]["Metric"]["Value"]

            if temperature < 0 or temperature > 35:
                return "It's cold outside"
            elif wind_speed > 50:
                return "It's windy outside"
            elif precipitation_probability > 70:
                return "It's rainy outside"
            else:
                return "The weather is nice"

        except (KeyError, IndexError):
            raise Exception("Invalid current weather data")
