import heapq
class Solution:
    def highest_3_elements(self, arr, k): # Not correct
        heap = []
        for value in arr:
            if len(heap) < k:
                heapq.heappush(heap, value)
            else:
                heapq.heappushpop(heap, value)
        return heap[0] * heap[1] * heap[2]

    def max3e(self, arr, k):
        arr = sorted(arr)

        hi3 = arr[-1] * arr[-2] * arr[-3]
        lo2hi1 = arr[0] * arr[1] * arr[-1]
        return max(hi3, lo2hi1)

#Time complexity: O(n* log(n))
#Space complexity: O(k)
solution = Solution()
print(solution.max3e([0,-1,10, 5, 7], 3))