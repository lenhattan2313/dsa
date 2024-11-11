class Solution:
    def insertion_sort(self, arr):
        n = len(arr)
        if n < 2:
            return arr
        i = 1
        while i < n:
            curr = arr[i]
            j = i - 1
            if arr[j] < curr:
                continue
            while j >= 0 and arr[j] > curr:
                arr[j + 1] = arr[j]
                j-= 1
            arr[j + 1] = curr
            i += 1
        return arr

solution = Solution()
print(solution.insertion_sort([9, 2, 4, 1, 5]))

