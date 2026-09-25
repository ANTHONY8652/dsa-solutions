# 3550. Smallest Index With Digit Sum Equal to Index
# Approach: Loop through array, calculate digit sum using str conversion
# Time complexity: O(n)

def SmallestIndex(nums):
    for i in range(len(nums)):
        digit_sum = sum(int(d) for d in str(nums[i]))

        if digit_sum == i:
            return i
    return -1

print(SmallestIndex([1,5,6,4]))
print(SmallestIndex([2,3,1]))
print(SmallestIndex([1,10,11]))

class Solution:
    def smallestIndex(self, nums:list[int]) -> int:
        for i, num in enumerate(nums):
            if sum(int(d) for d in str(num)) == i:
                return i
        return -1

[1,3,2]
