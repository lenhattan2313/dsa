class Solution:
    def insertion_sort(self, arr):
        n = len(arr)
        if n < 2:
            return arr

        for i in range(1, n):
            cur = arr[i]
            j = i - 1
            if arr[j] < cur:
                continue
            while j >= 0 and arr[j] >= cur:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = cur
        return arr

solution = Solution()
print(solution.insertion_sort([9, 2, 4, 1, 5]))

