from flask import Flask,render_template,request
from forgerock_exercise import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/stock', methods=['POST', 'GET'])
def stock():
	if request.method == 'GET':
		return render_template('stonks.html')
	else:
		stock_sym=request.form['stock']
		days_before=request.form['days']
		parsed_data=time_series(stock_sym, days_before)
		average_closing_price=averaging_out(parsed_data, days_before)
		return render_template('average.html', avg_close=average_closing_price, list=parsed_data, sym=stock_sym, days=days_before)

app.run(host='localhost', port=8081)
