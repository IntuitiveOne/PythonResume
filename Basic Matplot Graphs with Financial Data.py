import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt  #
pd.options.display.float_format = '{:.4f}'.format #limiting number of decimals for easier data reading

start = "2013-03-15"     
end   = "2023-03-15" #defining time period of data observing

symbol = ["AMZN", "AAPL", "MSFT"]

df = yf.download(symbol, start, end) #using yahoo api to get data of selected stocks("symbols")

df.to_csv("multi_assets.csv") #saving data to csv file

df = pd.read_csv("multi_assets.csv", header = [0, 1], index_col = 0, parse_dates =[0]) #loading up and formatting csv file data into a data frame to use

close = df.Close.copy() #just taking the closing stock valuations before turning it into a graph without messing with the original data frame

close.MSFT.dropna().plot(figsize = (15, 8), fontsize = 13) #graph of just the microsoft stock
plt.legend(fontsize = 13)
plt.show()


close.dropna().plot(figsize = (15, 8), fontsize = 13) #graph of all the stocks we took data of
plt.legend(fontsize = 13)
plt.show()
