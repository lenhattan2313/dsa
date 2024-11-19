class Solution:
    def isSubsequence(self, s, t):
        i = j = 0
        n = len(t)
        while i < n:
            if s[j] == t[i]:
                j+= 1
            i+= 1

        return j == len(s)

solution = Solution()
print(solution.isSubsequence("abc", "ahsgdc"))