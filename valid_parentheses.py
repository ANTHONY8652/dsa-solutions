class Solution:
    def isValid(self, s:str) -> bool:
        if len(s) % 2 != 0: return False
        
        stack = []
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}
        
        for c in s:
            print("char:", c, "stack before:", stack)
            if c in "([{":
                stack.append(c)
            elif stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
            
            print("stack after:", stack)
        
        return not stack

solution = Solution()
print(solution.isValid("(())"))