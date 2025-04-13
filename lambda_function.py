import json
import requests

def lambda_handler(event, context):
    # Get the city from the query parameters, default to 'London'
    city = event.get('queryStringParameters', {}).get('city', 'London')
    
    # Your OpenWeatherMap API key (replace with your actual key)
    api_key = '646be78b2a1ceb9182f3bbe0a48f541a'
    
    # Build the request URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Make the API call
    response = requests.get(url)
    data = response.json()
    
    # Prepare and return the response
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'city': city,
            'temperature': data.get('main', {}).get('temp', 'N/A'),
            'weather': data.get('weather', [{}])[0].get('description', 'N/A')
        })
    }
