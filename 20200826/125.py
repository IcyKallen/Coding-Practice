class Solution:
    def isPalindrome(self, s: str) -> bool:
        to_list = list(s.lower())
        char_list = []
        for char_ in to_list:
            if char_.isalnum():
                char_list.append(char_)
        for i in range(len(char_list)):
            if char_list[i] != char_list[len(char_list)-1-i]:
                return False
            if i > len(char_list)-1-i:
                break
        return True

#s.lower() string变小写
#list(s) 按字母分成list,不用split()
#isalnum() 字符串由数字和字母构成
#isdigit() 由数字构成
#isalpha() 由字母构成