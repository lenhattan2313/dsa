class Solution:
    def threeSum(self, nums):
        i, j = 0, len(nums) - 1
        ans = []
        while i < j - 1:
            for k in range(i + 1, j):
                if nums[i] + nums[j] + nums[k] == 0:
                    return ans.append([nums[i], nums[j], nums[k]])
            i += 1

        i = 0
        while i < j - 1:
            for k in range(i + 1, j):
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])
            j -= 1

        return ans

