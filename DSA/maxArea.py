
#Leecode 11
class Solution:
    def maxArea(self, height):
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] > height[right]:
                right -=1
            else:
                left += 1
        return max_area

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7])) #49