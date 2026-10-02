class Solution:
    def removeDuplicates(self, nums:list[int]) -> int:
        # The list is SORTED, so duplicates sit next to each other.
        # Two pointers:
        #   left  = where the next UNIQUE value should be written
        #   right = scout that walks through the whole list
        # nums[0] is always unique (nothing before it), so left starts at 1
        left = 1
        
        # right starts at 1 because we compare each number with the one before it
        for right in range(1, len(nums)):
            # different from the previous number = a new unique value
            if nums[right] != nums[right - 1]:
                # write it at the "next unique" spot
                nums[left] = nums[right]
                # move the spot forward for the next unique value
                left += 1
            # left now equals the count of unique values
            # BUG: this return is inside the for loop, so it exits after the
            # first pass. It should be dedented to line up with "for".
            return left 




#FASTEST SOLUTION removes or reduces overall overhead
class SOLUTION(object):
    def removeDuplicates(self, nums):
        # l = index of the LAST unique value found so far (starts at nums[0])
        l = 0
        n = len(nums)
        
        # c = scout that walks through the list (starts at 0, comparing
        # nums[0] with itself on the first pass is harmless)
        for c in range(n):
            # scout found something different from the last unique value
            if nums[l] != nums[c]:
                # move l forward to the next slot...
                l += 1
                # ...and put the new unique value there
                nums[l] = nums[c]
            # l is an INDEX (starts at 0), so count = l + 1
            # BUG: same problem, this return is inside the loop. Dedent it
            # to line up with "for".
            return l + 1