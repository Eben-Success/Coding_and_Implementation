# Generate Regular Numbers
# Daily Coding Problem Page: 111

"""
A regular number in mathematics is defined as one which
evenly divides some power of 60. Equivently, we can say that a regular number is one
whose only prime divisor are 2, 3 and 5.

These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according to the diatonic scale.

Given an integer n, write a program that generates, in order, the first n regular numbers.

NAIVE APPROACH
A naive solution would be to first generate all powers of 2, 3 and 5 up to some
stopping point, and then find every product we can obtain from multiplying one power
from each group. We can then sort these products and take the first n to find our solution.

COMPLEXITIES
Time: O(n^3 * logn): 3 for loops and the sorted function
"""

# BRUTE FORCE
def regular_numbers(n):
    twos = [2**i for i in range(n)]
    threes = [3**i for i in range(n)]
    fives = [5**i for i in range(n)]

    result = set()

    for two in twos:
        for three in threes:
            for five in fives:
                result.add(two * three * five)

    return sorted(result)[:n]

print(regular_numbers(6))

# OPTIMAL APPROACH USING MIN-HEAP
# Time: O(nlogn)

import heapq

def regular_numbers(n):
    solution = [1]
    last = 0; count = 0

    while count < n:
        x = heapq.heappop(solution)
        if x > last:
            yield x
            last = x; count += 1
            heapq.heappush(solution, 2 * x)
            heapq.heappush(solution, 3 * x)
            heapq.heappush(solution, 5 * x)