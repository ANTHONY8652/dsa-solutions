class Solution:
    def isPalindrome(self, x:str) -> bool:
        #Check if the number reversed from last to first is equal to the original number if yes returns teru else False
        return str(x) == str(x)[::-1]
        
    
solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(141))
print(solution.isPalindrome(67))

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #If x < 0 it can't be a palindrome close it out early
        if x < 0:
            return False
        original = x
        reversed_number = 0

        while x > 0:
            #Modulo grabs the last digit 
            #Peel off the last digit
            last_digit = x % 10
            #Shift reversed number left by one place and drop last_digit into the gap
            reversed_number = (reversed_number * 10) + last_digit
            #Floor division chops off that last digit
            x = x // 10
        
        return original == reversed_number
        