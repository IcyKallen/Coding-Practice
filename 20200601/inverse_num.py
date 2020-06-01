class Solution:
    def reverse(self, x: int) -> int:
        int_str = str(x)
        if x > 0:
            if(int(int_str[::-1]) > 2**31 - 1):
                return 0
            else:
                return int(int_str[::-1])
        elif x < 0:
            if(0-int(int_str[:0:-1]) < -2**31):
                return 0
            else:
                return 0-int(int_str[:0:-1])
        else:
            return 0
        