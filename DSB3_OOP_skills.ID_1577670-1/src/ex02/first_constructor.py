import sys
import os
class Research:
    def __init__(self, file_path):
        self.file_path = file_path
        
    
    def file_reader(self):
        try:
            with open(self.file_path, 'r') as red:
                return red.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"
        
def main():
    if len(sys.argv) != 2:
        print("Usage: python first_constructor.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    
    # Проверка существования файла
    if not os.path.exists(file_path):
        print(f"Error : {file_path} not exists")
        sys.exit(1)
    if not os.path.isfile(file_path):
        print(f"Error: {file_path} is not file")
        sys.exit(1)
    res = Research(file_path)
    print(res.file_reader())
    
if __name__ == "__main__":
    main()