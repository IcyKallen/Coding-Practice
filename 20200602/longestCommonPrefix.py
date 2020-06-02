class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        first_str = strs[0]
        commonprefix = []
        for i in range(len(first_str)):
            for each_word in strs:
                if i >= len(each_word) or first_str[i] != each_word[i]:
                    return ''.join(commonprefix)
                else:
                    continue
            commonprefix.append(first_str[i])
        return ''.join(commonprefix)