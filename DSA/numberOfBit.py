class Solution:
    def numberOfBit(self, num):
        ans = 0
        while num != 0:
            ans+= 1
            num &= num - 1
        return ans

# Time complexity: O(one)
# Space complexity: O(1)
solution = Solution()
print(solution.numberOfBit(11))