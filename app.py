from phone_number_validator_toolkit.validator import PhoneNumberValidator

from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# Import the environ module from the os package

# Import from your PyPI package

app = Flask(__name__)
# Replace with your actual API key
api_key = os.getenv('PHONE_NUMBER_VALIDATOR_API_KEY')
validator = PhoneNumberValidator(api_key)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/validate', methods=['POST'])
def validate():
    phone_number = request.form.get('phone_number')
    country_code = request.form.get('country_code')
    try:
        is_valid = validator.validate(phone_number, country_code)
        return jsonify({"valid": is_valid})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
