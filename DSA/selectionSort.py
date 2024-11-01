class Solution:
    def selection_sort(self, arr):
        n = len(arr)
        if n < 2:
            return arr
        for i in range(n - 1):
            minIndex = i
            for j in range(i + 1, n):
                if arr[minIndex] > arr[j]:
                    minIndex = j
            if minIndex != i:
                [arr[minIndex], arr[i]] = [arr[i], arr[minIndex]]
        return arr


solution = Solution()
print(solution.selection_sort([9, 2, 4, 1, 5]))
