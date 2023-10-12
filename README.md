# Weather Forecast App

 This is a simple Python application that provides weather forecasts for the next days based on user input. It uses the Streamlit framework for the user interface, fetches weather data from the OpenWeatherMap API, and displays temperature and sky conditions using Plotly and image integration.

### How it Works
- The user enters a location in the provided text input field.

- The user selects whether they want to see temperature or sky conditions.

- The user selects the number of days to forecast (up to 5 days).

- The application fetches weather data for the specified location using the OpenWeatherMap API.

- Based on the user's choice (temperature or sky), the application displays either a line chart of temperature or a set of images representing the sky conditions for the specified days.

### Prerequisites
Before running the code, you need to obtain an API key from OpenWeatherMap. You can sign up for a free API key on their website.

### Usage
Clone the repository to your local machine.
git clone https://github.com/yourusername/weather-forecast-app.git

### Install the required Python packages by running:

pip install -r requirements.txt

### Replace the APIkey variable in the code with your OpenWeatherMap API key.

### Run the application:

streamlit run weather_forecast_app.py

Enter a location, select the data type, and set the forecast days to view the weather forecast.


### Technologies Used
- Streamlit: For creating the user interface.

- Plotly: For creating interactive charts.

- OpenWeatherMap API: For retrieving weather data.