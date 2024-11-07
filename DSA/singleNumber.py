class Solution:
    def singleNumber(self, nums):
        n = len(nums)
        ans = {}
        for p in nums:
            ans[p] = ans.get(p, 0) + 1

        return min(ans, key=ans.get)


solution = Solution()
print(solution.singleNumber([3,1,3,2,2]))