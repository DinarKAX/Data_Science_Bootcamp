import timeit

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

if __name__ == "__main__":
    ex00 = Ex00()
    time_loop = timeit.timeit(ex00.loop_version, number=9000000)
    time_list = timeit.timeit(ex00.list_version, number=9000000)
    time_map = timeit.timeit(ex00.map_version, number=9000000)
    
    results = {
        "loop": time_loop,
        "list": time_list,
        "map": time_map
    }

    dict_sorted = sorted(results.items(), key=lambda item: item[1])
    print(results.items())
    if dict_sorted[0][0] == "loop":
        print("it is better to use a loop")
    elif dict_sorted[0][0] == "list":
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a map")
    
    print(f"{dict_sorted[0][1]} vs {dict_sorted[1][1]} vs {dict_sorted[2][1]}")