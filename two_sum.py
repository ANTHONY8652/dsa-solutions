def two_sum(nums,target):
    #Store the seen numbers 
    seen = {}
    
    #Enumerating through the list, storing their various indexes
    for i, num in enumerate(nums):
        #We are going to subtract the current number with the number we have and see if they add up to target 
        needed = target - num
        
        #If the number we need is in seen we return it as well as it's index 
        if needed in seen:
            #Return seen number and needed number and their indexes
            return [seen[needed], i]
        #Log and save the seen number as well as it's index
        seen[num] = i
    
    #If all set conditions evaluate to true return the indexes of the numbers
    return[]

two_sum([3, 2, 4], 6)


"""
def find_max(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

find_max([2,4,5,6,7])
"""

"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], i]
            seen[num] = i
        return[]
        
"""