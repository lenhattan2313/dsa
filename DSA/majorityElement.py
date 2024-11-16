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

# counter = Counter(nums)
        # for key, value in counter.items():
        #     if value > len(nums) / 2:
        #         return key
        # return 0
        # hash = {}
        # ans = majority = 0
        # for i in nums:
        #     hash[i] = hash.get(i, 0) + 1
        #     if hash[i] > majority:
        #         ans = i
        #         majority = hash[i]
        # hash = defaultdict(int)
        # for n in nums:
        #     hash[n] += 1
        #     if(hash[n] > len(nums) // 2):
        #         return n
        # return None
        #
        # candidate = 0
        # count = 0
        # for n in nums:
        #     if count == 0:
        #         candidate = n
        #     count += 1 if n == candidate else -1
        # return candidate
# Example usage
solution = Solution()
print(solution.majorityElement([3, 2, 3]))  # Output: 3
print(solution.majorityElement([2, 2, 2,2,2,4]))  # Output: 2
