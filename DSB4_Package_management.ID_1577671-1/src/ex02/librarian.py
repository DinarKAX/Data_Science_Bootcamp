#!/usr/bin/env python3

import os

def main():
    try:
        if 'VIRTUAL_ENV' not in os.environ:
            raise Exception("Not in virtual environment")
        os.system('pip3 install Beautifulsoup4 pytest')
        os.system('pip freeze')
        os.system('pip freeze > requirements.txt')
    except KeyError:
        print('Wrong enviroment')
    return

if __name__ == '__main__':
    main()