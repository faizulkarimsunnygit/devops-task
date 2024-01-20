from flask import Flask, jsonify, request
from datetime import datetime
from healthcheck import HealthCheck
import requests

app = Flask(__name__)

# Entry Point
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Weather Info
@app.route('/api/info', methods=['GET'])
def get_server_info():
    hostname = request.headers.get('Host')

    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    version = "1.0"
    
    weather_api_key = 'B6ZP3ZRVFN3DJAJD7LJQGCN49'
    weather_api_url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Dhaka%2CBangladesh?unitGroup=metric&key={weather_api_key}&contentType=json'

    response = requests.get(weather_api_url)
    apiResponse = response.json()
    
    weather = {
        apiResponse['address'] : apiResponse['currentConditions']
    }

    return jsonify({
        'hostname': hostname,
        'datetime': current_datetime,
        'version': version,
        'weather_info': weather
    })

# Health Check
health = HealthCheck()

def redis_availablity():
    client = _redis_client()
    info = client.info()
    return True, "redis ok"

health.add_check(redis_availablity)

app.add_url_rule("/api/healthcheck", "healthcheck", view_func=lambda: health.run())

if __name__ == '__main__':
    app.run(debug=True)

