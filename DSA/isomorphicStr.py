class Solution:
    def isomorphicStr(self, s, t):
        char_s = {}
        char_t = {}
        for i, j in zip(s, t):
            if i not in char_s:
                char_s[i] = j
            elif char_s[i] != j:
                return False

            if j not in char_t:
                char_t[j] = i
            elif char_t[j] != i:
                return False

        return True


solution = Solution()
print(solution.isomorphicStr('egg', 'add'))