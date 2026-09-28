# 242. Valid Anagram (Easy) - Arrays & Hashing
# Two words are anagrams if every letter appears the same number of times in both.

class Solution:
    # Approach 1: two hash maps (my solution)
    # Time:  O(n)  - one pass through the strings, dict get/set is O(1)
    # Space: O(k)  - k = distinct letters, max 26 for lowercase a-z
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        if countS == countT:
            return True
        return False

    # Approach 2: sorting
    # Time:  O(n log n) - sorted() is the slow part
    # Space: O(n)       - sorted() makes a new list
    def isAnagram_sorted(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

#Counter method was quite interesting and fascinated me
from collections import Counter
class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        return Counter(s) == Counter(t)