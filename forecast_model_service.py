class ForecastModelService:

    def check_weather(self, current_weather):
        """
        температура ниже 0°C или выше 35°C,
        скорость ветра выше 50 км/ч,
        вероятность осадков выше 70%
        """
        if current_weather is None:
            return "Unable to retrieve current weather"

        try:
            if (
                current_weather[0]["Temperature"]["Metric"]["Value"] < 0
                or current_weather[0]["Temperature"]["Metric"]["Value"] > 35
            ):
                return "It's cold outside"
            elif current_weather[0]["Wind"]["Metric"]["Speed"]["Value"] > 50:
                return "It's windy outside"
            elif (
                current_weather[0]["PrecipitationSummary"]["Metric"]["Probability"] > 70
            ):
                return "It's rainy outside"
            else:
                return "It's sunny outside"

        except (KeyError, IndexError):
            return "Invalid weather data"
