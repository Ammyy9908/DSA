def getDuplicates(string):
    dict = {}
    for i in string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict



print(getDuplicates('hqhqhhhhhh'))