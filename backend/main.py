import math
from decimal import Decimal
from datetime import datetime

from flask import Flask, request, jsonify
from flask_cors import CORS 


app = Flask(__name__)
CORS(app)

# This dictionary will act as a simple in-memory storage for readings
readings = []
factorial_cache = {}

# Endpoint for submitting a reading
@app.route('/submit_reading', methods=['POST'])
def submit_reading():
    try:
        # Get the data from the request JSON
        data = request.get_json()

        # Extract the reading and timestamp from the data
        reading = int(data['reading'])
        timestamp_str = data['timestamp']

        # Parse the timestamp string into a datetime object
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M')

        # Store the reading and timestamp
        readings.append({'reading': reading, 'timestamp': timestamp_str})

        return jsonify({'status': 'success'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Endpoint for retrieving the factorials of all readings
@app.route('/get_factorials', methods=['GET'])
def get_factorials():
    try:
        # Calculate factorials for all readings
        factorials = []
        for reading_data in readings:
            reading = reading_data['reading']
            factorial_result = calculate_factorial(reading)
            factorials.append({'reading': reading, 'factorial': factorial_result})

        return jsonify({'status': 'success', 'factorials': factorials})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

def calculate_factorial(n):
    """
    Returns the factorial of n.

    Utilises a cache optimisation if n has been seen before.

    The factorial loop decrements back from n to make use of
    the factorial cache.

    Parameters:
        n (int): The number of factorials to be calculated

    Returns:
        result (Decimal): the result of the factorial calculation 
        in Decimal format. Decimal is used to handle very large integers
        being cast to a string.
    """
    if n < 0:
        return None  # Factorial is undefined for negative numbers
    
    result = Decimal(1)

    for i in range(n, 1, -1):
        # Retrieve result from cache if exists
        if i in factorial_cache:
            result *= factorial_cache.get(i)
            break
        result *= Decimal(i)
    
    # Store result of calculate_factorial(n) for any subsequent runs
    factorial_cache[n] = result
    return result

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
