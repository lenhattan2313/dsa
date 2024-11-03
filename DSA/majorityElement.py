class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        # Phase 1: Find a candidate
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        # Phase 2: Verify the candidate (optional if we assume there's always a majority element)
        if nums.count(candidate) > len(nums) // 2:
            return candidate
        else:
            return None  # No majority element found

# Example usage
solution = Solution()
print(solution.majorityElement([3, 2, 3]))  # Output: 3
print(solution.majorityElement([2, 2, 2,2,2,4]))  # Output: 2
