import sys
import os
from random import randint

class Research:
    def __init__(self, file_path):
        self.file_path = file_path
        
    
    def file_reader(self, has_header = True):
        
        try:
            with open(self.file_path, 'r') as red:
                lines = red.readlines()
            res = []
            start_i = 1 if has_header else 0
            for i in range(start_i, len(lines)):
                line = lines[i].strip()
                if line: # Проверка что строка не пустая
                    values = line.split(',')
                    try:
                        row = [int(val.strip()) for val in values]
                        res.append (row)
                    except ValueError:
                        print( f"Error: Cannot convert to number in line: {line}")
                        continue # Пропускаем некорректную строку
            return res
                    
        except FileNotFoundError:
            return(f"Error : file '{self.file_path}' not found.")
        except Exception as e:
            return f"Error reading file: {str(e)}"
        
    class Calculations:
        def __init__(self, data):
            self.data = data
        def counts(self):
            if not self.data:
                return [0, 0]
            heads_count = sum(row[0] for row in self.data)
            tails_count = sum(row[1] for row in self.data)
            return [heads_count, tails_count]

        def fractions(self):
            count_res = self.counts()
            all_heads_tails = count_res[0] + count_res[1]
            if all_heads_tails == 0:
                return [0.0, 0.0]
            head_proc = count_res[0] / all_heads_tails
            tails_proc = count_res[1] / all_heads_tails
            return [head_proc, tails_proc]
        
    class Analytics(Calculations):
        def __init__(self, data):
            super().__init__(data)
        def predict_random(self, num_predictions):
            predictions = []
            for _ in range(num_predictions):
                if randint(0, 1):
                    predictions.append([1, 0])
                else:
                    predictions.append([0, 1])
            return predictions
        def predict_last(self):
            if not self.data:
                return []
            else:
                return self.data[-1]
        
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
    try:
        research = Research(file_path)
        data = research.file_reader()

        calculations = research.Calculations(data)

        count_res = calculations.counts()

        fraction_res = calculations.fractions()
        
        analitics = research.Analytics(data) #создаем объект Analytics (наследник Calculations)
        
        prediction_random = analitics.predict_random(3) #рандом орел или решка
        
        prediction_last = analitics.predict_last() #предсказать последний
        
        print(data)
        print(*count_res)
        print(*[f"{x:.4f}" for x in fraction_res])
        print(prediction_random)
        print(prediction_last)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
        
if __name__ == "__main__":
    main()