from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    api_key = '<ff3c2b875499602404d24c263c700b9c>'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    return jsonify({'temperature': temperature, 'description': description})

if __name__ == '__main__':
    app.run(debug=True)
