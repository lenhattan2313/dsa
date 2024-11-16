import heapq
class Solution:
    def last_stone_weight(self, arr):
        for i in range(len(arr)):
            arr[i] = -arr[i]

        heapq.heapify(arr)
        while len(arr) > 1:
            max_num = -heapq.heappop(arr)
            next_max = -heapq.heappop(arr)

            if max_num != next_max:
                heapq.heappush(arr, - max_num + next_max)

        return -arr[0] if arr else 0
#Time complexity: O(n)
#Space complexity: O(1)
solution = Solution()
print(solution.last_stone_weight([2,7,4,1,8,1]))