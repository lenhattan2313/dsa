
class Solution:
    def distribute_candy(self, arr):
        n = len(arr)
        dp = sorted((x, i) for i, x in enumerate(arr))
        candies = [1] * n
        print(dp)
        for _, i in dp:
            if i > 0 and arr[i] < arr[i - 1]:
                candies[i] = max(candies[i], candies[i-1] +1)
            if i < n - 1 and arr[i] > arr[i+1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
# Time complexity: O(n log(n))
# Space complexity: O(n)
solution = Solution()
print(solution.distribute_candy([0.3, 0.7, 0.4, 0.1]))