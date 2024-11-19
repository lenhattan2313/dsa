from collections import defaultdict


class Solution:
    def canContructor(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        hash = defaultdict(int)
        for i in magazine:
            hash[i] += 1
        for i in ransomNote:
            if i in hash and hash[i] > 0:
                hash[i] -= 1
            else:
                return False
        return True

    def canContructor2(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False

        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False
        return True


solution = Solution()
print(solution.canContructor('aa', 'aab'))