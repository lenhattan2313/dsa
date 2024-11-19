class Solution:
    def isPalindrome(self, s):
        s = ''.join(s.strip().split()).lower()
        left, right = 0, len(s) - 1
        while left < right:

            while left < right and not s[left].isalnum():
                left+= 1
            while right > left and not s[right].isalnum():
                right-= 1
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return False


        return True

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))