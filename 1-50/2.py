# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        initial_node = previous_node = ListNode(None)
        sum = 0
        while l1 or l2 or sum:
            if l1 is not None:
                sum = sum + l1.val
            if l2 is not None:
                sum = sum + l2.val
            current_node = ListNode(sum%10)
            sum = sum//10
            previous_node.next = current_node
            previous_node = current_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return initial_node.next

# 可以直接从第一个节点开始加，这样得到结果
# 仔细考虑边界情况
