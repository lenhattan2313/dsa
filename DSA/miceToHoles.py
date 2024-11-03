class Solution:
    def mice_to_holes(self, A, B):
        A.sort()
        B.sort()
        ans = 0
        for a,b in zip(A, B):
            ans = max(ans, abs(a-b))
        return ans


# Time complexity: O(n log(n))
# Space complexity: O(1)
solution = Solution()
print(solution.mice_to_holes([3, 2, -4], [0,-2,4]))