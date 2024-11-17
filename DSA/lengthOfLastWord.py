class Solution:
    def lengthOfLastWord(self, str):
        return len(str.strip().split()[-1])