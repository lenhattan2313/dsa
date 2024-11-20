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

    def twoSumII(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return []

    def twoSum(self, nums, target):
        hash = {}
        for i in range(len(nums)):
                if nums[i] in hash:
                    return [hash[nums[i]], i]
                hash[target - nums[i]] = i

        return None



solution  = Solution()
print(solution.twoSum([2, 3, 4], 6))

# -4 -1 -1 0 1 2
