import timeit
import random
from collections import Counter

class Ex04:
    def __init__(self):
        self.data = [random.randint(0,100) for _ in range(1000000)]
    def count_with_dict(self):
        dict = {}
        for i in self.data:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        return dict
    
    def most_valuable(self):
        dict = {}
        for i in self.data:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        sorted_dict = sorted(dict.items(), key=lambda x:x[1], reverse= True)
        return sorted_dict[:10]

    def count_with_dict_with_counter(self):
        counter = Counter(self.data)
        return Counter
    
    def most_valuable(self):
        counter = Counter(self.data)
        return counter.most_common(10)
        
    def run_benchmark(self):
        print(f'my function: {timeit.timeit(self.count_with_dict, number=10)}')
        print(f'Counter: {timeit.timeit(self.most_valuable, number=10)}')
        print(f'my top: {timeit.timeit(self.count_with_dict_with_counter, number=10)}')
        print(f'Counter\'s top: {timeit.timeit(self.most_valuable, number=10)}')
        
if __name__ == "__main__":
    try:
        prac =  Ex04()
        prac.run_benchmark() 
    except Exception as e:
        print(f"Error: {e}")