from flask import Blueprint, render_template, request, flash
from flask_login import current_user, login_required
from .models import User, Stock
import nasdaqdatalink
from . import NASDAQ_KEY
import pandas as pd

nasdaqdatalink.read_key(filename='mywebsite/nasdaqapikey')
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', user=current_user)

@views.route('/mystocks', methods=['GET', 'POST'])
@login_required
def mystocks():
    if request.method == 'GET':
        return render_template('mystocks.html', user=current_user)
    else:
        # TODO Check validity of stock ticker
        # Save ticker to user's list of stocks to track
        ticker = request.form.get('ticker')
        if len(ticker) < 3:
            flash("Invalid stock ticker")
        else:
            df = nasdaqdatalink.get_table('WIKI/PRICES', qopts = { 'columns': ['ticker', 'date', 'close'] }, ticker = ticker, date = { 'gte': '2020-01-01', 'lte': '2024-02-13' })
            if not df.empty:
                print(df.head())
                print("Printing database")
        #new_stock = Stock(ticker, current_user.id)
        # Check if exists in user's stocks
        return render_template('mystocks.html', user=current_user)