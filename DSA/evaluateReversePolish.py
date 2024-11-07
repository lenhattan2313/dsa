class Solution:
    def evaluateReversePolist(self, tokens):
        stack = []
        for t in tokens:
            if t in '+-*/':
                b, a = stack.pop(), stack.pop()
                if t == '*':
                    stack.append(a * b)
                elif t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(t))
        return stack[0]

solution = Solution()
print(solution.evaluateReversePolist(["2", "1", "+", "3", "*"]))