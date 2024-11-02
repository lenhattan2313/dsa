class Solution:
    def disjointInvervals(self, arr):
        arr.sort(key=lambda x: x[1])
        count = 1
        prev_s, prev_e = arr[0]

        for s, e in arr:
            if s <= prev_s:
                pass
            else:
                prev_s, prev_e = s, e
                count += 1

        return count

#Time complexity: O(n log(n))
#Space complexity: O(1)
solution = Solution()
print(solution.disjointInvervals([[1,2], [2, 10],[4,6]]))
