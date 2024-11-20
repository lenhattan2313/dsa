from collections import Counter, defaultdict


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

    def anagram(self, s, t):
        hash = defaultdict(int)
        for i in s:
            hash[i] += 1

        for j in t:
            if j in hash and hash[j] > 0:
                hash[j] -= 1
            else:
                return False
        return all(value == 0 for value in hash.values())


solution = Solution()
print(solution.anagram("anagram", "nagaram"))