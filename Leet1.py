def removeKdigit(num, k):
    
    stack = []
    
    for c in num:
        while k > 0 and stack and stack[-1]  > c:
            k -= 1
            stack.pop()
        stack.append(c)
    
    stack = stack[:len(stack) - k]
    res = "".join(stack)
    return str(int(res)) if res else "0"


num = "10200"

print(removeKdigit(num, k=3))