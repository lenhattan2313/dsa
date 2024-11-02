class Solution:
    def meeting_rooms(self, arr):
        dp = []
        for s,e in arr:
            dp.append((s, 1))
            dp.append((e, -1))

        # dp.sort(key=lambda x: x[0])
        dp.sort()
        cur = 0
        result = 0
        for _,v in dp:
            cur+= v
            result = max(cur, result)

        return result
# Time complexity: O(n log(n))
# Space complexity: O(n)
solution = Solution()
print(solution.meeting_rooms([[5,10], [15, 20], [0,30]]))