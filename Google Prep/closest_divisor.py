def closestDivisors(num):
    def helper(n):
        i = int((n**0.5))
        while i > 0:
            if (n % i == 0):
                return [i, n // i]
            i -= 1
        return [n, 1]

    res1 = helper(num+1)
    res2= helper(num + 2)
