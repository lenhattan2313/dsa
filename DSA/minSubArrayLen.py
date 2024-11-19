class Solution:
    def minSubArrayLen(self, target, nums):
        left = right = 0
        n = len(nums)
        ans = float('inf')
        while left < n:
            while right < n and sum(nums[left:right + 1]) < target:
                right += 1
            while left < n and sum(nums[left:right + 1]) >= target:
                ans = min(ans, right - left + 1)
                left += 1
            left += 1
        return 0 if ans == float('inf') else ans

