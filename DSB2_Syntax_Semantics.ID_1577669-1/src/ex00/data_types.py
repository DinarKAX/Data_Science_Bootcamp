def data_types():
    int_a = 0
    string_a = "dfs"
    float_a = 2.2
    bool_a = True
    list_a = [1,2,3]
    dict_a = {1:2, 2:3}
    tuple_a = (1, 2, 3)    
    set_a = set()
    
    t = [int_a, string_a, float_a, bool_a, list_a, dict_a, tuple_a, set_a]


    res = []
    for i in t:
        res.append(type(i).__name__)
    print(res)
    
if __name__ == '__main__':
    data_types()