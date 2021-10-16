
import yfinance as yf
import streamlit as st
import pandas as pd
#from PIL import Image
import datetime


st.write("""
# Simple Stock Price App

""")

st.sidebar.header("Enter symbol")


tickerSymbol = 'GOOGL'
symbol = st.sidebar.text_area("", tickerSymbol)

st.sidebar.header('Enter dates')

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
ayearago = yesterday - datetime.timedelta(days=365)
start_date = st.sidebar.date_input('Start date', ayearago)
end_date = st.sidebar.date_input('End date', yesterday)


st.write("""### Current symbol:
	""", symbol)


tickerData = yf.Ticker(symbol)
tickerDf = tickerData.history(period='1d', start=str(start_date), end=str(end_date))

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)	


def filedownload(df):
	csv = df.to_csv()
	href = f'<a href="data:file/csv;{csv}"  download="summary.csv"> Download CSV File</a>'
	return href

ticker_described = tickerDf.describe()
ticker_described.reset_index(level=0, inplace=True)

ticker_described.columns = ['feature']+list(ticker_described.columns)[1:]
#st.write(['feature']+list(ticker_described.columns))

st.write(ticker_described)
st.markdown(filedownload(ticker_described), unsafe_allow_html=True)


##image = Image.open('logo-app2.jpg')
##st.image(image, use_column_width=False, width=400)
