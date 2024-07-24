Python Flask backend with HTML Template bootstrapped with Matcha.css.

Utilising a phone validation package that I built and published with Poetry.

Clone the Repository:
git clone https://github.com/example/myproject.git
cd myproject

Install Dependencies:
poetry install

Add as a Dependency to Another Project:
If you want to add myproject as a dependency to another Poetry-managed project:
cd ../otherproject
poetry add ../myproject


To run the Project:
> poetry run gunicorn -c gunicorn_config.py app:app