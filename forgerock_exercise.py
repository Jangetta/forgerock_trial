from alpha_vantage.timeseries import TimeSeries
import pandas as pd

def time_series(stock_sym, days):
	days=int(days) 
	api_key = open('api_key.txt').read()
	daily_series = TimeSeries(api_key, output_format='pandas')
	data, meta = daily_series.get_daily(stock_sym, outputsize='compact')
	
	stock_values = ['open', 'high', 'low', 'close', 'volume']
	data.columns = stock_values

	dated_values = data.head(days).copy()
	
	closing_data = dated_values.close.to_list()

	return(closing_data)

def averaging_out(list_price, days):
	tempsum = 0

	days=int(days)
	
	for data in list_price:
		tempsum=tempsum+data

	means=tempsum/days

	return(means)
