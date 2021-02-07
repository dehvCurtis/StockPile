import pandas

# add filename downloaded from nasdaq
file = 'nasdaq_screener_1612650590475.csv'

csv_file = pandas.read_csv(file)

symbol_column = csv_file.Symbol

symbol_list = []

# removes tickers with multiple classes as noted with '^' in nasdaq list (example: ABR^A)
for ticker in symbol_column:
    symbol_list.append(ticker)
    if '^' in ticker:
        symbol_list.pop()

# write tickers to new file
with open('stocks.txt', 'w') as ticker_file:
    for ticker in symbol_list:
        ticker_file.write(f'{ticker}\n')