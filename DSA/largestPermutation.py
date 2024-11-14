class Solution:
    def largest_permutation(self, arr, k):
        i = 0
        _max = len(arr)

        d = {x : i for i, x in enumerate(arr)}
        while k and i < len(arr):
            j = d[_max]
            if i == j:
                pass
            else:
                arr[i], arr[j] = arr[j], arr[i]
                d[arr[i]], d[arr[j]] = d[arr[j]], d[arr[i]]
                k-= 1
            i+=1
            _max -= 1
        return arr

#1053. Previous Permutation With One Swap
    def prevPermOpt1(self, arr):
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i-= 1
        if i < 0:
            return arr

        j = n - 1
        while j > i and (arr[j] >= arr[i] or arr[j] == arr[j - 1]):
            j-= 1
        arr[j], arr[i] = arr[i], arr[j]
        return arr

#Time complexity: O(n)
#Space complexity: O(1)
solution = Solution()
print(solution.largest_permutation([1, 3, 4, 2], 1))