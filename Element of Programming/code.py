import sys


def count_bit(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


print(sys.float_info)