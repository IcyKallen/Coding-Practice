class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        listA, listB = list(A), list(B)
        if len(listA) != len(listB):
            return False
        diff_pos = []
        for i in range(len(listA)):
            if listA[i] != listB[i]:
                diff_pos.append(i)
        if len(diff_pos) == 2:
            if listA[diff_pos[0]] == listB[diff_pos[1]] and listA[diff_pos[1]] == listB[diff_pos[0]]:
                return True
            else:
                return False
        elif len(diff_pos) == 0:
            if len(listA) == len(set(listA)):
                return False
            else:
                return True
        else:
            return False

# 注意边界情况
# 注意set使用