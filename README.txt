# Yasmin Gil
# Creating web app mvp
# notes

Hello! and welcome to GirlStocks, my fullstack development project that makes informed decisions about stock activity.
This locally hosted website supports account creation and authentication, integration with roughViz API for chart visualizations and local database storage.
Features to be implemented: Integration with NASDAQ API for stock activity, pandas for modeling stock activity and roughViz for presenting findings

Techstack: Python/Flask, HTML/css, Javascript, SQLaclchemy


1. Set up virtual environment and download packages

py -m venv venv 
venv\Scripts\activate
pip install flask
pip install flask-sqlalchemy
pip install flask-login
pip install py-roughviz
pip install pydantic
pip install "pymongo[srv]"
