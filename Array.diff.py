def array_diff(a, b):
    new_array = []
    for i in range(len(a)):
        if a[i] not in b:
            new_array.append(a[i])
    return new_array
