import pandas as pd
import yfinance as yf
pd.options.display.float_format = '{:.4f}'.format #limiting number of decimals for easier data reading

start = "2013-03-15"     
end   = "2023-03-18" #defining time period of data observing

symbol = ["AMZN"]

amzn = yf.download(symbol, start, end) #using yahoo api to get data of selected stock("symbol")

amzn.Close.to_csv("amzn.csv")

amzn = pd.read_csv("amzn.csv", header = [0, 1], index_col = 0, parse_dates =[0])

print(amzn)

amzn["Returns"] = amzn.pct_change(periods = 1)

print(amzn)

am = amzn.Returns.mean() #Arithmetic Mean Return
print(am)

deviation = amzn.Returns.std() #Risk/Volatility (Standard Deviation of Returns)
print(deviation)

multiple = (1 + amzn.Returns).prod() #Investment Multiple
print(multiple)

start = amzn.index[0] #Compound Annual Growth Rate
end = amzn.index[-1]
td = end - start
print(td) 
td_years = td.days / 365.25
print(td_years)
cagr = multiple**(1 / td_years) -1 
print(cagr)

n = amzn.Returns.count()
geo_mean = multiple**(1/n) - 1 # Daily Geometric Mean Return
print(geo_mean)