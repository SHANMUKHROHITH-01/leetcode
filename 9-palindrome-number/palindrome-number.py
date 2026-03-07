class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
    
        div = 1
        temp = x
        while temp >= 10 * div:
            div *= 10
        
        while div > 1:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x % div) // 10  
            div //= 100          
        
        return True
