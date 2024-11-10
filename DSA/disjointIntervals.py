class Solution:
    def disjointInvervals(self, arr):
        arr.sort(key=lambda x: x[1])
        count = 1
        prev_s, prev_e = arr[0]

        for s, e in arr:
            if s <= prev_e:
                pass
            else:
                prev_s, prev_e = s, e
                count += 1

        return count

    def eraseOverlapIntervals(self, arr) -> int:
        count = 0
        prev_e = arr[0][1]

        for i in range(1, len(arr)):
            if arr[i][0] >= prev_e:
                prev_e = arr[i][1]
            else:
                count += 1
        return count
#Time complexity: O(n log(n))
#Space complexity: O(1)
solution = Solution()
print(solution.disjointInvervals([[1,2], [2, 10],[4,6], [3, 4]]))
[1,2], [3, 4], [4, 6], [2, 10]