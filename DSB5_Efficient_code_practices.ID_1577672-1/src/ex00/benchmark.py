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

    def list_comperhension(self):
        return [email for email in self.emails if email.endswith(self.domain)]

if __name__ == "__main__":
    ex00 = Ex00()
    time_loop = timeit.timeit(ex00.loop_version,number = 9000000)
    time_list = timeit.timeit(ex00.list_comperhension,number = 9000000)

    if time_loop >= time_list:
        print("it is better to use a list comprehension") 
    else:
        print("it is better to use a loop")
    
    print(f'{min(time_loop, time_list)}' + ' vs ' + 
        f'{max(time_loop, time_list)}')