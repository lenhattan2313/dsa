class Solution:
    def largest_permutation(self, arr, k):
        i = 0
        _max = len(arr)
        d = { x: i for i, x in enumerate(arr)}
        while k and i < len(arr):
            j = d[_max]
            print(i,j, d)
            if i == j:
                pass
            else:
                k -= 1
                arr[i], arr[j] = arr[j], arr[i]
                d[arr[i]], d[arr[j]] = d[arr[j]], d[arr[i]]

            i+=1
            _max -= 1
        return arr

#Time complexity: O(n)
#Space complexity: O(1)
solution = Solution()
print(solution.largest_permutation([1, 3, 4, 2], 1))