"""
1. Two Sum
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {} #dict number -> index, stores each number you've already passed, along with where you saw it
        
        for i, num in enumerate(nums): #Check the number as well as it's index
            needed = target - num #Look for the needed number that is minused from the current number with the target
            if needed in seen: #Check before storing
                return [seen[needed], i] #Retun index
            seen[num] = i #Return key value pairs
        return[]

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,3], 6))
print(solution.twoSum([3,2,4], 6))
        
