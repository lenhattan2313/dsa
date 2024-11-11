import heapq
class Solution:
    def highest_k_elements(self, arr, k):
        heap = []
        for s in arr:
            if len(heap) < k:
                heapq.heappush(heap, s)
            else:
                heapq.heappushpop(heap, s)
        return heap
    def max_k_elements(self, arr, k):
        arr = sorted(arr)
        hi3 = arr[-1] * arr[-2] * arr[-3]
        lo2hi1 = arr[0] * arr[1] * arr[-1]
        return max(hi3, lo2hi1)


#Time complexity: O(n* log(n))
#Space complexity: O(k)
solution = Solution()
print(solution.max_k_elements([0,-1,10, 1, -7], 3))

