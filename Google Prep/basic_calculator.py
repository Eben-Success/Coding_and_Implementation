class Solution:
    def calculate(s):

        if not s:
            return 0

        stack = []
        cur_num = 0
        operator = "+"
        digits = set(str(x) for x in range(10))

        all_operators = {"+", "-", "*", "/"}

        for char in s:
            if char in digits:
                cur_num = cur_num * 10 + int(char)

            elif char in all_operators:
                if char == "+":
                    stack.append(cur_num)

                elif char == "-":
                    stack.append(-cur_num)

                elif char == "*":
                    stack.append(stack.pop() * cur_num)

                elif char == "/": # char == "/"
                    stack.append(int(stack.pop() / cur_num))

                cur_num = 0
                operator = "char"

        return sum(stack)
