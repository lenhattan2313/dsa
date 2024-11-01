class Solution:
    def bubble_sort(self, arr):
        n = len(arr)
        if n < 2:
            return arr
        for i in range(n):
            swap = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    [arr[j + 1], arr[j]] = [arr[j], arr[j + 1]]
                    swap = True
            if not swap:
                break
        return arr


solution = Solution()
print(solution.bubble_sort([9, 2, 4, 1, 5]))
