# Time: O(2^n) | Space: O(n) -> call stacks

# Without memoization

# def fib(n):
#     if n <= 2:
#         return 1
    
#     return fib(n - 1) + fib(n - 2)

# Memoization
# Hashmap: key will be arg to fn, value will be return value
# Time: O(n) | Space: O(n)

def fib(n, memo = {}):
    if n in memo: return memo[n]
    if n <= 2:
        return 1
    
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


print(fib(6))
print(fib(7))
print(fib(8))
print(fib(500))