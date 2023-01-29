# A function that divides to numbers such that
# n = a * b

def divisor(n):
    i = int((n**0.5))

    while i > 0:
        if (n % i == 0):
            return [i, n // i]
        i -= 1
    return [n, 1]