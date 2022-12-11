# Check if a decimal integer is  a palindrome.
# Page 47

"""
If the input is negative, we can't find its palindrome
"""

"""
Brute force approach is to convert the input into a string.
And use two pointers to compare the characters.
Converting to string takes a Space of O(n) and Time of O(n).

With the optimal approach, we can use log to find the answer.
Least significant digit is x mod 10, and the most significant digit is
x/10^n-1
"""

import math


def is_palindrome_number(x):
    if x <= 0:
        return x == 0

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (num_digits - 1)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask  # Remove the most significant digit of x
        x //= 10  # Remove the least significant digit of x
        msd_mask //= 100
