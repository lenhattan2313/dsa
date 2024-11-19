class Solution:
    def wordPattern(self, pattern, s):

        s = s.split()
        char_s = {}
        char_pattern = {}

        for p, word in zip(pattern, s):
            if p in char_pattern:
                if char_pattern[p] != word:
                    return False
            else:
                char_pattern[p] = word
            if word in char_s:
                if char_s[word] != p:
                    return False
            else:
                char_s[word] = p
        return True


solution = Solution()
print(solution.wordPattern('abba', "dog cat cat dog"))