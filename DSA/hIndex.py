from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        backet = [0] * (n + 1)

        for i in range(n):
            backet[min(citations[i], n)] += 1
        cumulative_papers = 0
        for i in range(n, -1, -1):
            cumulative_papers += backet[i]
            if cumulative_papers >= i:
                return i

        return 0

solution = Solution()
print(solution.hIndex([3,8,5,2,3]))