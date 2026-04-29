import sys
import time
import psutil
import os

def get_memory_usage(file_path):
    lines = read_file(file_path)
    for line in lines:
        pass
    
    usage = psutil.Process()
    print(f'Peak memory usage= {usage.memory_info().rss / 1073741824} GB')
    print(f'User Mode Time + System Mode Time = {usage.cpu_times().user + usage.cpu_times().system}s')
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        if not os.access(file_path, os.R_OK):
            raise OSError("Can't open file")
        for line in file:
            yield line

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("You need 2 arguments")
            sys.exit(1)
        else:
            get_memory_usage(sys.argv[1])
    except Exception as e:
        print(f"{e}")