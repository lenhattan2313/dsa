class Solution:
    def is_perfect_square(self, n):
        left = 1
        right = n

        while left < right:
            mid = (right + left) // 2
            if mid * mid > n:
                right = mid - 1
            elif mid * mid < n:
                left = mid + 1
            else:
                return True
        return False

