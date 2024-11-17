from typing import  List
from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 2
        for i in range(2, n):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k+= 1
        print(nums)
        return k

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = k % len(nums)
        # if k != 0:
        #     nums[:k], nums[k:] = nums[-k:], nums[:-k]
        # return nums
        n = len(nums)
        k %= n
        rotated = [0] * n
        for i in range(n):
            rotated[(i + k) % n] = nums[i]
        for i in range(n):
            nums[i] = rotated[i]
        return nums
#Time complexity: O(n)
#Space complexity: O(1)
solution = Solution()
# print(solution.removeDuplicates([0,0,1,1,1,1,2,3,3]))

# print(solution.majorityElement([8,8 ,7,7,7]))
print(solution.rotate([1,2,3,4,5,6,7], 2))
