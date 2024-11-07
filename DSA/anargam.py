from collections import Counter


class Solution:
    def is_anagram(self, A, B):
        if len(A) != len(B):
            return False
        # solution 1: O(nlog(n))
        # return sorted(A) == sorted(B)

        #solution 2: O(n)
        # return Counter(A) == Counter(B)

        #solution 3: O(n)

        hash = {}
        for i in range(len(A)):
            char = A[i]
            hash[char] = hash.get(char, 0) + 1
        for i in range(len(B)):
            char = B[i]
            if char not in hash:
                return False
            if char in hash:
                hash[char] -= 1

            if hash.get(char) == 0:
                hash.pop(char)
        return not hash





solution = Solution()
print(solution.is_anagram("dear", "raad"))