class Solution:
    def rotateArr(self, nums, k):
        n = len(nums)
        k %= n
        # rotated = [0] * n
        #
        # for i in range(n):
        #     rotated[(i + k) % n] = nums[i]
        # for i in range(n):
        #     nums[i] = rotated[i]
        # return rotated

        if k != 0:
            nums[:k] , nums[k:]  = nums[-k:], nums[:-k]

        return nums

solution = Solution()
print(solution.rotateArr([1,2,3,4,5,6,7], 3))

