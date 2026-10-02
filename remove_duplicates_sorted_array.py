class Solution:
    def removeDuplicates(self, nums:list[int]) -> int:
        left = 1
        
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
            return left 




#FASTEST SOLUTION removes or reduces overall overhead
class SOLUTION(object):
    def removeDuplicates(self, nums):
        l = 0
        n = len(nums)
        
        for c in range(n):
            if nums[l] != nums[c]:
                l += 1
                nums[l] = nums[c]
            return l + 1
