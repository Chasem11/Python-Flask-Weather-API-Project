from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from config import API_KEY
import datetime
import requests

# Flask app initialization
app = Flask(__name__)
api = Api(app, version='1.0', title='Event Weather API',
          description='A simple API to get weather forecast for events')


# Swagger input model for event details
event_model = api.model('Event', {
    'event_name': fields.String(required=True, description='Name of the event'),
    'event_date': fields.String(required=True, description='Date of the event (YYYY-MM-DD)'),
    'event_time': fields.String(required=True, description='Time of the event (HH:MM)'),
    'event_location': fields.String(required=True, description='Location of the event (city)')
})

# Function to get weather information
def getWeather(event_location):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={event_location}&appid={API_KEY}&units=imperial"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None

# API route to get event weather
@api.route('/event-weather')
class EventWeather(Resource):
    @api.expect(event_model)
    def post(self):
        data = request.json

        event_name = data['event_name']
        event_date = data['event_date']
        event_time = data['event_time']
        event_location = data['event_location']
        
        datetime_str = f"{event_date} {event_time}"
        
        try:
            date_format = "%Y-%m-%d %H:%M"
            date_object = datetime.datetime.strptime(datetime_str, date_format)
            five_days_later = datetime.datetime.today() + datetime.timedelta(days=5)

            if date_object < datetime.datetime.today():
                return {"error": "The event date has already passed."}
            elif date_object > five_days_later:
                return {"error": "The event is more than 5 days in the future."}

        except ValueError:
            return {"error": "Incorrect data format, should be YYYY-MM-DD"}

        weather_info = getWeather(event_location)
        if not weather_info:
            return {"error": "Unable to retrieve weather information"}

        first_item_dt = datetime.datetime.strptime(weather_info['list'][0]['dt_txt'], "%Y-%m-%d %H:%M:%S")
        smallest_delta = abs(date_object - first_item_dt)
        closest_forecast = weather_info['list'][0]

        for item in weather_info['list']:
            item_dt = datetime.datetime.strptime(item['dt_txt'], "%Y-%m-%d %H:%M:%S")
            time_delta = abs(date_object - item_dt)
            if time_delta < smallest_delta:
                smallest_delta = time_delta
                closest_forecast = item

        forecast = closest_forecast['weather'][0]['description']
        temp = closest_forecast['main']['temp']

        return {
            "event_name": event_name,
            "event_location": event_location,
            "event_date": event_date,
            "event_time": event_time,
            "weather_forecast": forecast,
            "temperature": temp
        }

# Add resource to Flask app
api.add_resource(EventWeather, '/event-weather')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
