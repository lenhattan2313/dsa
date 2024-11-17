class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        i = 0
        while i < len(haystack) and needle != haystack[i:i + len(needle)]:
            i+= 1
        return i
solution = Solution()
print(solution.strStr( "adbutsad",  "sad"))