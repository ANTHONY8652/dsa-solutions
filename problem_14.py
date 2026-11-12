"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
class Solution:
    def longestcommonprefix(self, strs: list[str]) -> str:
        first = strs[0]
        for i in range (len(first)):
            for word in strs:
                if i >= len(word) or word[i] != first[i]:
                    return first[:i]
        return first
    
solution = Solution()
print(solution.longestcommonprefix(["flower","flow","flight"]))
print(solution.longestcommonprefix(["dog","racecar","car"]))