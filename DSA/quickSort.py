class Solution:
    def quick_sort(self, arr, low, high):
        if low < high:
            sorted_index = self.partition(arr, low, high)
            self.quick_sort(arr, low, sorted_index - 1)
            self.quick_sort(arr, sorted_index + 1, high)
        return arr

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high
        while i <= j:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] > pivot:
                j -= 1

            if j > i:
                [arr[i], arr[j]] = [arr[j], arr[i]]
                i += 1
                j -= 1
        [arr[j], arr[low]] = [arr[low], arr[j]]

        return j

solution = Solution()
print(solution.quick_sort([9, 2, 4, 1, 5], 0 , 4))
