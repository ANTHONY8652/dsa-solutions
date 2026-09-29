#Time complexity O(N)
#Concatenating takes O(N)
#Searching takes O(N) (normally)

class Solution:
    def rotate_string(self, s:str, goal:str) -> bool:
        #CHeck if the length of s and goal are the same if they are not they can't be the same rotated
        if len(s) != len(goal):
            return False
        
        #Create a new string by concatenating 's' with itself
        doubled_string = s + s
        
        #Use find to search if 's' concatenated 's' contains goal anywhere
        return doubled_string.find(goal) != -1

solution=Solution()
print(solution.rotate_string("abcde", "cdeab"))
print(solution.rotate_string("abcde", "abced"))