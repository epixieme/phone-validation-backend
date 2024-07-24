# About

- Python Flask backend with HTML Template bootstrapped with Matcha.css. Utilising a phone validation package that I built and published with Poetry.

# Installation
1. Clone the Repository:
git clone https://github.com/example/myproject.git
cd myproject

2. Install Dependencies:
poetry install

3. Add as a Dependency to Another Project:
If you want to add myproject as a dependency to another Poetry-managed project:
cd ../otherproject
poetry add ../myproject


4. To run the Project:
> poetry run gunicorn -c gunicorn_config.py app:app
