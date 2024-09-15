def tickers_to_dict(filename):
    tickers = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if ':' in line:
                parts = line.split(':')

            key, value = parts
            tickers[key.strip()] = value.strip()
            
    return tickers

def name_to_symbol(name, ticker_dict):
    try:
        return ticker_dict[name]
    except KeyError:
        return None

def symbol_to_name(symbol, ticker_dict):
    try:
        for key, value in ticker_dict.items():
            if value == symbol:
                return key
    except ValueError:
        return None
    


tickers = tickers_to_dict('tickers.txt')

name = input('Enter Company name: ')
print("Ticker symbol: {}".format(name_to_symbol(name, tickers)))

symbol = input('Enter Ticker symbol: ')
print("Company name: {}".format(symbol_to_name(symbol, tickers)))