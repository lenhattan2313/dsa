
class Solution:
    def reverseWords(self, s):
        arr = s.strip().split()
        ans = []
        for i in range(len(arr) - 1, -1, -1):
            ans.append(arr[i])

        return ' '.join(ans)
    def twoPointer(self, s):
        s = s.strip().split()
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        return ' '.join(s)

solution = Solution()

print(solution.reverseWords("the sky is blue"))
