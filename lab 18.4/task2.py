import requests
import json

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for bad responses

        weather_data = response.json()

        # Check if the API returned a valid city
        if weather_data.get("cod") != 200:
            print(json.dumps({
                "error": f"City not found or invalid request",
                "details": weather_data
            }, indent=4))
        else:
            print(json.dumps(weather_data, indent=4))

    except requests.exceptions.HTTPError as http_err:
        print(json.dumps({
            "error": "HTTP error occurred",
            "details": str(http_err)
        }, indent=4))
    except requests.exceptions.ConnectionError:
        print(json.dumps({
            "error": "Connection error occurred",
            "details": "Unable to connect to the weather service"
        }, indent=4))
    except requests.exceptions.Timeout:
        print(json.dumps({
            "error": "Request timed out",
            "details": "The weather API did not respond in time"
        }, indent=4))
    except requests.exceptions.RequestException as e:
        print(json.dumps({
            "error": "An unknown error occurred",
            "details": str(e)
        }, indent=4))

# Example usage:
# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
get_weather("warangal", "dcbc2131855f54ce74f1caefa8239f2f")
