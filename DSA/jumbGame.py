from typing import List
class Solution:
    def jumb(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n - 1
        for i in range(n - 1, -1, -1):
            if nums[i] + i >= target:
                target = i

        return target == 0

        # gas = 0
        # for n in nums:
        #     if gas < 0:
        #         return False
        #     elif n > gas:
        #         gas = n

        #     gas-= 1
        # return True
    def jumpII(self, nums: List[int]) -> int:
        n = len(nums)
        near = far = jumb = 0
        while far < n - 1:
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])
            near = far + 1
            far = farthest
            jumb += 1

        return jumb