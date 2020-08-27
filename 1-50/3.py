class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length_s = len(s)
        if length_s == 0:
            return 0
        max_length = 0
        for i in range(length_s):
            previous_char = set()
            starting = i
            current_length = 0
            while starting < length_s and s[starting] not in previous_char:
                if starting != length_s - 1:
                    previous_char.add(s[starting])
                    starting = starting +1
                    current_length = current_length + 1
                else:
                    current_length = current_length + 1
                    return max(max_length, current_length)
            max_length = max(max_length, current_length)

# 这个没什么技巧，从第一个开始数就行了