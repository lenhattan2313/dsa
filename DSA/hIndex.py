from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        bucket = [0] * (n + 1)

        for i in range(len(bucket)):
            bucket[min(citations[i], n)] += 1

        cumulative_paper = 0
        for h_index in range(len(bucket) -1, -1, -1):
            cumulative_paper += bucket[h_index]
            if cumulative_paper >= h_index:
                return h_index
        return 0

solution = Solution()
print(solution.hIndex([3,8,5,2,3]))