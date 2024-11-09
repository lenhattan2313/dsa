class Solution:
    def product(self, nums):
        n = len(nums)
        ans = [1] * n
        left = 1
        for i in range(n):
            ans[i] *= left
            left *= nums[i]
        right = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans

#Time: O(n)
#Space: O(n)
solution = Solution()
print(solution.product([1,2,3,4]))
