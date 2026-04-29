from functools import reduce
import timeit
import sys

class Ex00:
    def __init__(self, arg, number, count):
        self.arg = arg
        self.number = int(number)
        self.count = int(count)
        
    def loop_method(self): 
        sum = 0
        for i in range(int(self.count)):
            sum = sum + ((i + 1) * (i + 1))
        return sum

    def reduce(self):
        def sum(prev, next):
            return prev + next**2
        return(reduce(sum, range(1, int(self.count) + 1)))
        
    def run_benchmark(self):
        if self.arg == "loop":
            time_taken = timeit.timeit(self.loop_method, number=self.number)
        elif self.arg == "reduce":
            time_taken = timeit.timeit(self.reduce, number=self.number)
        else:
            print("Invalid method. Use: loop or reduce")
            return
        print(time_taken)
        
if __name__ == "__main__":
    
    try:
        if len(sys.argv) == 4:
            prac =  Ex00(sys.argv[1], sys.argv[2], sys.argv[3])
            prac.run_benchmark() 
        else:
            raise Exception("Wrong quantity of args")
    except Exception as e:
        print(f"Error: {e}")