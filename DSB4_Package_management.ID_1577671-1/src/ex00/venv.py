#!/usr/bin/env python3
import os

def get_virtual_env():
    # Получаем путь к виртуальной среде из переменной окружения
    venv_path = os.environ.get('VIRTUAL_ENV')
    
    if venv_path:
        print(f"Your current virtual env is {venv_path}")
    else:
        print("No virtual environment is currently active")

if __name__ == "__main__":
    get_virtual_env()

#python3 -m venv test
#source test/bin/activate
#chmod +x venv.py
#venv.py
#./venv.py
#deactivate