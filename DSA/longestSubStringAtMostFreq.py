from collections import defaultdict


class Solution:
    def longestSubStringAtMostFreq(self, s, k):
        char_map = defaultdict(int)
        longest = left = 0
        n = len(s)
        for right in range(n):
            char_map[s[right]] += 1
            while char_map[s[right]] > k:
                char_map[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
        print(char_map)
        return longest

solution = Solution()
print(solution.longestSubStringAtMostFreq("geeksforgeeks", 2))