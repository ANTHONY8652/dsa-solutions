class Solution:
    def maxDepth(self, s:str) -> str:
        #Initialise current to 0
        current = 0
        #Initialise reset to 0
        reset = 0
        
        for c in s:
            if c == "(":
                #Increment character by one
                reset += 1
            if c == ")":
                #Decrement character by 1
                reset -= 1
            #Return the max increment we counted from both current and reset
            current = max(current, reset)
        #Return the max nested parentheses we found
        return current