class Solution:
    def peak_element(self, arr):
        n = len(arr)
        if n == 0:
            return None
        if n == 1:
            return 0  # Only one element is considered a peak by default

            # Check the first element
        if arr[0] > arr[1]:
            return 0

            # Check the last element
        if arr[n - 1] > arr[n - 2]:
            return n - 1

        for i in range(1, n - 1):
            if arr[i] > arr[i-1] and arr[i] > arr[i +1]:
                return i
# Time complexity O(n)
# Space complexity O(1)

    def find_peak_element(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left
# Time complexity O(log n)
# Space complexity O(1)

solution = Solution()
print(solution.find_peak_element([1,2,3,1]))