def Fibonaaci(n):
    if n == 0 or n == 1:
        return n
    else:
        return Fibonaaci(n - 1) + Fibonaaci(n - 2)