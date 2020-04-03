def sort_array(source_array):
    new_list = []
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            new_list.append(source_array[i])
            source_array[i] = '-'
    new_list.sort()
    j = 0
    while j != len(new_list):
        for i in range(len(source_array)):
            if source_array[i] == '-':
                source_array[i] = new_list[j]
                j += 1
    return source_array
