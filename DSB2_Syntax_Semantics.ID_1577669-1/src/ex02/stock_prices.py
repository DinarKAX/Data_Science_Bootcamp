import sys
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


def search():
    
    name_comp = sys.argv
    if len(name_comp) != 2:
        return 
    
    name_comp = name_comp[1].capitalize()
    
    if name_comp in COMPANIES:
        print(STOCKS[COMPANIES[name_comp]])
    else:
        print("Unknown company")
        
if __name__ == '__main__':
        search()