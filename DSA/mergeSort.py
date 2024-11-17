from typing import List


class Solution:
    def merge_sort(self, arr):
        n = len(arr)
        if n < 2:
            return arr
        left = 0
        right = n - 1
        mid = n // 2
        left_arr = self.merge_sort(arr[left:mid])
        right_arr = self.merge_sort(arr[mid:right + 1])
        return self.merge(left_arr, right_arr)

    def merge(self, left, right):
        i = 0
        j = 0
        sorted_arr = []
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                sorted_arr.append(right[j])
                j += 1
            else:
                sorted_arr.append(left[i])
                i += 1
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr

    # Leetcode: 88
    def mergeSortedArray(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        mindex = m - 1
        nindex = n - 1
        right = m + n - 1
        while nindex >= 0:
            if mindex >= 0 and nums1[mindex] > nums2[nindex]:
                nums1[right] = nums1[mindex]
                mindex -= 1
            else:
                nums1[right] = nums2[nindex]
                nindex -= 1
            right -= 1

    # Leetcode: 27
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k

    # Leetcode 26
    def removeDuplicates(self, nums: list[int]) -> int:
        # if not nums:
        #     return 0
        # j = 1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         nums[j] = nums[i]
        #         j += 1
        #
        # return j
        i, k = 0, 0
        n = len(nums)
        while i < n:
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            nums[k] = nums[i]
            k += 1
            i += 1
        return k

    # Leetcode 80
    def removeDuplicateII(self, nums):
        count = 0
        n = len(nums)
        k = 2
        for i in range(2, n):
            if nums[i] != nums[i - 2]:
                nums[k] = nums[i]
                k+= 1
        print(nums)
        return k







solution = Solution()
print(solution.mergeSortedArray([1, 2, 3, 0, 0, 0], 3, [2, 4, 5], 3))
print(solution.removeDuplicateII([0,0,1,1,1,1,2,3,3]))