# 217. Contains Duplicate
# Approach: Early return loop with a seen set
# For each number check if it exists in seen — if yes duplicate found return True
# If not add it to seen and continue
# Time complexity: O(n) — one pass through the array
# Space complexity: O(n) — seen set grows with input
# Best case: O(1) — duplicate found at index 1
# Worst case: O(n) — no duplicates, entire array processed

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

solution = Solution()
print(solution.containsDuplicate([1,2,3,4,1]))
print(solution.containsDuplicate([1,2,3,1]))
print(solution.containsDuplicate([1,2,3,4,5,6]))