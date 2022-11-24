def recursive_summation(n):
    if n <= 1:
        return n
    return recursive_summation(n-1) + n

print(recursive_summation(10))