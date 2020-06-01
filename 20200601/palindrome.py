class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return(x == x[::-1])

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x!=0 and x%10==0):
            return False
        elif x == 0:
            return True
        else:
            reverse_x = 0
            while x > reverse_x:
                remainder = x % 10
                reverse_x = reverse_x * 10 + remainder
                x = x // 10
            if reverse_x == x or reverse_x//10 == x:
                return True
            else:
                return False
