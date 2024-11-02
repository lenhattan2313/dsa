class Solution:
    def bulbs(self, arr):
        cost = 0
        for b in arr:
            if cost % 2 == 0: b = b
            else: b = not b

            if b % 2 == 1: continue
            else: cost += 1

        return cost

#Time complexity: O(n)
#Space complexity: O(1)
solution = Solution()
print(solution.bulbs([1,0,1]))