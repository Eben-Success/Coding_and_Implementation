def decimal_to_binary(n):
    if n < 0:
        return "Must be a positive integer"
    digit = str(n % 2)
    return decimal_to_binary(n // 2) + digit if n > 1 else  digit