from flask import Flask, render_template, request, redirect

from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['Alpha-Vantage-API-key']

import requests
import json 
key = s3
ticker = 'AAPL'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}'.format(ticker, key)
response = requests.get(url)
print(response.json()) 

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
