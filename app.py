import yfinance as yf
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def info():
    ticker = request.args.get('ticker')
    stock = yf.Ticker(ticker)
    info = stock.info
    return jsonify(info)

@app.route('/news')
def info():
    ticker = request.args.get('ticker')
    stock = yf.Ticker(ticker)
    news = stock.news
    return jsonify(news)


