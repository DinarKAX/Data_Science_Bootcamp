def search():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
        ]
   
    outp = dict()
    for itiem in list_of_tuples:
        if itiem[1] not in outp:
            outp[itiem[1]] = [itiem[0]]
        else:
            outp[itiem[1]].append(itiem[0])
        
    for key, value in outp.items():
        for v in value:
            print(f'\'{key}\' : \'{v}\'')
    return


if __name__ == "__main__":
    search()
    
    