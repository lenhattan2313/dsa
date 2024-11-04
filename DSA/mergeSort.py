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
        right_arr = self.merge_sort(arr[mid:right +1])
        return self.merge(left_arr, right_arr)

    def merge(self, left, right):
        i = 0
        j = 0
        sorted_arr = []
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                sorted_arr.append(right[j])
                j+=1
            else:
                sorted_arr.append(left[i])
                i+=1
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m
        j = n
        while i > 0 and j > 0:
            if nums1[i - 1] > nums2[j - 1]:
                nums1[i + j - 1] = nums1[i - 1]
                i -= 1

            else:
                nums1[i + j - 1] = nums2[j - 1]
                j -= 1


        return nums1

    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        count = n
        while i < n:
            if nums[i] == val:
                nums[i] = 0
                count -= 1
            i += 1
        return count

    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j+=1

        return j



solution = Solution()
print(solution.removeDuplicates([1,2,2,3]))



