class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        left = 0
        cur = ""
        for right in range(n):
            cur += s[right]
            while s[right] in cur[left:right]:
                left += 1
            ans = max(ans, right - left + 1)
        return ans

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash = {}
        for i, j in zip(s, t):
            if i not in hash and j not in hash:
                hash[i] = j
            elif hash[i] != j:
                return False
        return True

