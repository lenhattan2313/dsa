# Given an array arr[] consisting of N positive integers representing the ratings of N children,
# the task is to find the minimum number of candies required for distributing to N children
# such that every child gets at least one candy
# and the children having the higher rating get more candies than its neighbours.
class Solution:
    def distribute_candy(self, arr):
        n = len(arr)
        candies = [1] * n
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                candies[i] = candies[i - 1] + 1
        print(candies)
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        print(candies)
        return sum(candies)
# Time complexity: O(n)
# Space complexity: O(n)
solution = Solution()
print(solution.distribute_candy([1,7,4,3,1]))