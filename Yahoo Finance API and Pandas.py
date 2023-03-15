import pandas as pd
import yfinance as yf #yahoo finance api

start = "2013-01-01" #Defining Time Period                
end   = "2023-01-31"

symbol = "MSFT" #Choosing a stock to examine(we could put any stock here yahoo finance has access to)



df = yf.download(symbol, start, end) # defining the dataframe to download and storing it into a csv file
df
df.to_csv("microsoft_data.csv")

msft_stock = pd.read_csv("microsoft_data.csv", parse_dates= ["Date"], index_col = "Date") #defining the variable as the csv file for use



print(msft_stock.head()) #Example Methods we could call with the pandas libary

yearlystock = msft_stock.resample("Y").mean().round() #getting the average stock value of each year in our time frame

#just a simple template to demonstrate how to access financial data from yahoo finance and using the pandas libary, there are infinite possibilities


