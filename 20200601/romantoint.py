class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            if s[i] == 'M':
                result = result + 1000
            elif s[i] == 'D':
                result = result + 500
            elif s[i] == 'C':
                if i == len(s)-1:
                    result = result + 100
                elif s[i+1] =='M' or s[i+1] =='D':
                    result = result - 100
                else:
                    result = result + 100
            elif s[i] == 'L':
                result = result + 50
            elif s[i] == 'X':
                if i == len(s)-1:
                    result = result + 10
                elif s[i+1] =='C' or s[i+1] =='L':
                    result = result - 10
                else:
                    result = result + 10
            elif s[i] == 'V':
                result = result + 5
            elif s[i] == 'I':
                if i == len(s)-1:
                    result = result + 1
                elif s[i+1] =='X' or s[i+1] =='V':
                    result = result - 1
                else:
                    result = result + 1
        return result