import sys

def search():
    COMPANIES = {
            'Apple': 'AAPL',
            'Microsoft': 'MSFT',
            'Netflix': 'NFLX',
            'Tesla': 'TSLA',
            'Nokia': 'NOK'
    }
    STOCKS = {
            'AAPL': 287.73,
            'MSFT': 173.79,
            'NFLX': 416.90,
            'TSLA': 724.88,
            'NOK': 3.37
    }
    argument = sys.argv[1].replace(' ', '').split(',')
    for i in argument:
        company_name = i.capitalize()
        if company_name in COMPANIES:
            ticker = COMPANIES[company_name]
            price = STOCKS[ticker]
            print(f"{company_name} stock price is {price}")
        elif i.upper() in STOCKS:
            i = i.upper()
            for j in COMPANIES:
                if COMPANIES[j] == i:
                    print(i + " is a ticker symbol for " + j)
        else:
            print(i + " is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        search()
