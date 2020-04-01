def filter_list(l):
    new_array = []
    for i in l:
        if type(i) == int:
            new_array.append(i)
    return new_array
