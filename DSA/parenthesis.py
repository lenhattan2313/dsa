class Solution:
    def parenthesis(self, s):
        close_to_open = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in close_to_open:
                top_element = stack.pop() if stack else '#'
                if close_to_open[char] != top_element:
                    return False
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        return False

solution = Solution()
print(solution.parenthesis("()"))         # Output: True
print(solution.parenthesis("()[]{}"))     # Output: True
print(solution.parenthesis("(]"))         # Output: False
print(solution.parenthesis("([)]"))       # Output: False
print(solution.parenthesis("{[]}"))       # Output: True