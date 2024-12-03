from flask import Flask, render_template, request
from forecast_service import ForecastService
from forecast_model_service import ForecastModelService

app = Flask(__name__)

api_key = ""

forecast_service = ForecastService(apikey=api_key)
forecast_model_service = ForecastModelService()


@app.route("/", methods=["GET", "POST"])
def index():
    departure_current_weather = None
    departure_weather_check = None
    destination_current_weather = None
    destination_weather_check = None

    if request.method == "POST":
        departure = request.form.get("departure")
        destination = request.form.get("destination")
        if not departure or not destination:
            error = "Please enter a departure and destination city"
            return render_template("index.html", error=error)

        try:
            departure_location_key = forecast_service.get_location_key(departure)
        except Exception as e:
            return render_template("index.html", error=e)

        try:
            departure_current_weather = forecast_service.get_current_weather(
                departure_location_key
            )
        except Exception as e:
            return render_template("index.html", error=e)

        try:
            departure_weather_check = forecast_model_service.check_weather(
                departure_current_weather
            )
        except Exception as e:
            return render_template("index.html", error=e)

        try:
            destination_location_key = forecast_service.get_location_key(destination)
        except Exception as e:
            return render_template("index.html", error=e)

        try:
            destination_current_weather = forecast_service.get_current_weather(
                destination_location_key
            )
        except Exception as e:
            return render_template("index.html", error=e)

        try:
            destination_weather_check = forecast_model_service.check_weather(
                destination_current_weather
            )
        except Exception as e:
            return render_template("index.html", error=e)

    return render_template(
        "index.html",
        departure_current_weather=departure_current_weather,
        departure_weather_check=departure_weather_check,
        destination_current_weather=destination_current_weather,
        destination_weather_check=destination_weather_check,
    )


if __name__ == "__main__":
    app.run(debug=True)
