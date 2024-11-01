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


solution = Solution()
print(solution.merge_sort([9,4,1,3,5]))



