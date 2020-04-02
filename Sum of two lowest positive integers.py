def sum_two_smallest_numbers(numbers):
    new_array = [min(numbers)]
    numbers.remove(min(numbers))
    new_array.append(min(numbers))
    return new_array[0] + new_array[1]


numbers = [19, 5, 42, 2, 77]
print(sum_two_smallest_numbers(numbers))
