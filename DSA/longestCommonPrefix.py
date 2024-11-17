class Solution:
    #Leetcode 14
    def longestCommonPrefix(self, arr):
        ans = arr[0]
        n = len(arr)
        for i in range(1, n):
            word = arr[i]
            j = k = 0
            while j < len(ans) and k < len(word):
                if ans[j] == word[k]:
                    j += 1
                    k += 1
                else:
                    break
            if j < k:
                ans = ans[:j]
            else:
                ans = ans[:k]

        return ans

    def longest(self, arr):
        # Start with the first word as the initial prefix
        prefix = arr[0]

        for word in arr[1:]:
            # Find the minimum length between the current prefix and the word
            min_length = min(len(prefix), len(word))
            i = 0

            # Compare characters up to the minimum length
            while i < min_length and prefix[i] == word[i]:
                i += 1

            # Update the prefix to the common part
            prefix = prefix[:i]

            # If at any point the prefix becomes empty, there is no common prefix
            if not prefix:
                break

        return prefix


solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
