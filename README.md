# Python Flask Weather API Project

This project is a simple **Flask API** application that retrieves weather forecasts for a specified event location. It uses the **OpenWeatherMap API** to fetch weather data and calculates the time remaining until a user-defined event. The project also includes **Swagger API documentation** using **Flask-RESTX** for easy interaction with the API endpoints.

## Features

- **Event-Based Weather Forecast**: Retrieve weather information for a given event location.
- **Time Until Event**: Calculates and returns the time remaining until the event.
- **Swagger Documentation**: Provides interactive documentation via Swagger UI for testing the API endpoints directly in the browser.
- **Error Handling**: Handles errors for invalid dates, location not found, and server errors.

## Prerequisites

- **Python 3.7+**
- **Flask** and **Flask-RESTX** for building the API and generating Swagger documentation.
- **requests** for making HTTP requests to the OpenWeatherMap API.
- **python-dotenv** for managing environment variables (API key).

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/python-flask-weather-api-project.git
   cd python-flask-weather-api-project

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   
4. **Set Up OpenWeatherMap API Key**:
   - Create a `.env` file in the project root.
   - Add your **OpenWeatherMap API key** to the `.env` file:
     ```plaintext
     API_KEY=your_openweathermap_api_key
     ```
## Usage

1. **Run the Flask Application**:
   ```bash
   flask run
By default, the API will be available at `http://127.0.0.1:5000`.

## API Overview

This section briefly describes the API endpoints provided:

- **POST /event-weather**: Submits event details (name, date, time, location) and returns:
  - The time remaining until the event.
  - The weather forecast for the event location.

### Access Swagger Documentation:

- Open your browser and go to `http://127.0.0.1:5000/`.
- The Swagger UI will display the API endpoints and allow you to interact with them.

### Test the API Endpoint:

- In Swagger, expand the `/event-weather` POST endpoint.
- Click **Try it out** and enter the following details:
  - `event_name`: Name of the event.
  - `event_date`: Date of the event (format: `YYYY-MM-DD`).
  - `event_time`: Time of the event (format: `HH:MM`).
  - `event_location`: City where the event is taking place.
- Click **Execute** to retrieve the weather forecast and time remaining until the event.

## Troubleshooting

If you encounter issues, here are some common troubleshooting steps:

- **Environment Variables**: Ensure the `.env` file is set up correctly with your OpenWeatherMap API key.
- **Dependencies**: Double-check that all dependencies in `requirements.txt` are installed.
- **API Limitations**: OpenWeatherMap may impose rate limits. If you experience issues with data retrieval, consider waiting or upgrading to a paid plan.


   
