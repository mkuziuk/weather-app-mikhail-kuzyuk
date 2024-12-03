from flask import Flask, render_template, request
from forecast_service import ForecastService
from forecast_model_service import ForecastModelService

app = Flask(__name__)

api_key = "h7GlV7nA1YROwmECKW6BuJy0mYPaQxCJ"

forecast_service = ForecastService(apikey=api_key)
forecast_model_service = ForecastModelService()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        departure = request.form.get("departure")
        destination = request.form.get("destination")
        if not departure or not destination:
            # Handle the case where the form values are empty
            return render_template(
                "index.html", error="Please enter a departure and destination city"
            )
        location_key = forecast_service.get_location_key(destination)
        current_weather = forecast_service.get_current_weather(location_key)
        weather_check = forecast_model_service.check_weather(current_weather)
        return render_template(
            "index.html", current_weather=current_weather, weather_check=weather_check
        )
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
