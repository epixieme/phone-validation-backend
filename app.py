from flask import Flask, request, render_template, jsonify

# Import from your PyPI package
from phone_number_validator_toolkit.validator import PhoneNumberValidator

app = Flask(__name__)
# Replace with your actual API key
api_key = "num_live_9vBLFyhoA5fxSmBpfob2Fgi5zYCPtZZ8L0ZHLwPL"
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
