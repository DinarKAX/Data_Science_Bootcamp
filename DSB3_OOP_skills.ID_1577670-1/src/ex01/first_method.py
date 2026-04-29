class Research:
    def file_reader(self):
        with open('src/ex00/data.csv', 'r') as red:
            return red.read()
        
def main():
    res = Research()
    print(res.file_reader())
    
if __name__ == "__main__":
    main()