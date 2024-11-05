class Solution:
    def circularSentence(self, s: str):
        arr = s.split()
        for i in range(len(arr) - 1):
            if arr[i][-1] != arr[i+1][0]:
                return False
        return arr[0][0] == arr[-1][-1]

# Time complexity: O(n)
# Space complexity: O(n)
solution = Solution()
print(solution.circularSentence("elee ele"))