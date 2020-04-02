def digital_root(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    if sum > 9:
        return digital_root(sum)
    else:
        return sum
