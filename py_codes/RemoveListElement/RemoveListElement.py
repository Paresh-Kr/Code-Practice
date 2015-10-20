# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre_node = dummy
        cur_node = head
        while cur_node:
            if cur_node.val == val:
                pre_node.next = cur_node.next
            else:
                pre_node = cur_node
            cur_node = cur_node.next
        return dummy.next
