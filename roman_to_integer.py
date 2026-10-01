class Solution:
    def isRoman(self, s:str) -> int:
        if len(s) > 15: return False
        
        romans = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        
        total = 0
        
        for c in range(len(s)):
            if c + 1 < len(s) and romans[s[c]] < romans[s[c + 1]]: #Is there a next, and am I smaller than it ??
                total -= romans[s[c]] # yes -> minus
            else:
                total += romans[s[c]] # no -> plus
        return total
    

solution = Solution()
print(solution.isRoman("XIV"))
print(solution.isRoman("ILX"))
print(solution.isRoman("XIL"))
print(solution.isRoman("IXCM"))
print(solution.isRoman("VIMC"))
print(solution.isRoman("MCMXCIV"))
print(solution.isRoman("LVII"))
print(solution.isRoman("XLII"))
print(solution.isRoman("MCDXLIV"))