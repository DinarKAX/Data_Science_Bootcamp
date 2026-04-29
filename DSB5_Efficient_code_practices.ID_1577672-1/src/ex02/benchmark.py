import timeit
import sys

class Ex00:
    emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", 
    "anna@live.com", "philipp@gmail.com"] * 5
    domain = "@gmail.com"
    def loop_version(self):
        gmails = []
        for email in self.emails:
            if email.endswith(self.domain):
                gmails.append(email)
        return gmails

    def list_version(self):
        return [email for email in self.emails if email.endswith(self.domain)] 
    
    def map_version(self):
        def apply_func(c: str):
            if c.find(self.domain) != -1:
                return c
        return list(map(apply_func, self.emails))
    
    def filter_version(self):
        return list(filter(lambda email:email.endswith(self.domain), self.emails))
    
def run_benchmark(method_name, number):
    ex00 = Ex00()
    
    if method_name == "loop":
        time_taken = timeit.timeit(ex00.loop_version, number=number)
    elif method_name == "list_comprehension":
        time_taken = timeit.timeit(ex00.list_version, number=number)
    elif method_name == "map":
        time_taken = timeit.timeit(ex00.map_version, number=number)
    elif method_name == "filter":
        time_taken = timeit.timeit(ex00.filter_version, number=number)
    else:
        print("Invalid method. Use: loop, list_comprehension, or map")
        return
    print(time_taken)
    

if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print("Usage: python benchmark.py <method> <number>")
        sys.exit(1)
    elif len(sys.argv) == 3:
        method = sys.argv[1]
        try:
            numbers = int(sys.argv[2])
            run_benchmark(method, numbers)
        except ValueError:
            print("Error: second argument must be a number")
            sys.exit(1)
    else:
        print("Usage: python benchmark.py <method> <number>")
            
    
