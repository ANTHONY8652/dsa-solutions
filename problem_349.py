#Given two integer arrays nums1 and nums2, return an array of their intersection. 
#Each element in the result must be unique and you may return the result in any order.
"""
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""

class Solution:
    def intersection(self, nums1: list[int], nums2:list[int]) -> list[int]:
        return list(set(nums1).intersection(set(nums2)))
    
    #Brute Force 
    def intersect(self, nums1: list[int], nums2:list[int]) -> list[int]:
        result = []
        
        for num in nums1:
            if num in nums2 and num not in result:
                result.append(num)
        return result
    
    #iterate nums1, check membership in nums2, collect unique.
    #"Does it exist in the other list?" → make the other list a set
    def intersect2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set2 = set(nums2)
        result = set()
        
        for num in nums1:
            if num in set2:
                result.add(num)
        return list(result)

solution = Solution()
print(solution.intersection([1,2,2,1], [2,2]))
print(solution.intersection([4,9,5], [9,4,9,8,4]))
print(solution.intersect([1,2,2,1], [2,2]))
print(solution.intersect([4,9,5], [9,4,9,8,4]))
print(solution.intersect2([1,2,2,1], [2,2]))
print(solution.intersect2([4,9,5], [9,4,9,8,4]))

