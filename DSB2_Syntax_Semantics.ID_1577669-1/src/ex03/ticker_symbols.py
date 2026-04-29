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
    
    name_comp = name_comp[1].upper()
    flag = 1
    for key, item in COMPANIES.items():
        if item == name_comp:
            print(f"{key} {STOCKS[name_comp]}")
            flag = 0
            
    if flag:
        print("Unknown company")
if __name__ == '__main__':
        search()