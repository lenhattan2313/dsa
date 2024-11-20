from collections import defaultdict


class Solution:
    def longestSubStringWithAtMostKDistinct(self, s, k):
        n = len(s)
        longest = left = 0
        char_map = defaultdict(int)

        for right in range(n):
            char_map[s[right]] += 1

            while len(char_map.keys()) > k:
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0:
                    char_map.pop(s[left])
                left += 1


            longest = max(longest, right - left + 1)

        return longest

solution =Solution()
print(solution.longestSubStringWithAtMostKDistinct("aabbcc", 3))