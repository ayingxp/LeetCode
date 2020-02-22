"""
给定一个链表，两两交换其中相邻的结点，并返回交换后的链表。

注：不能只是单纯的改变结点内部的值，而是需要实际的进行结点交换
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def helper(start):
            if not start.next:
                return
            #start.val, end.val = end.val, start.val
            start.next = start.next.next
            start.next = start
            helper(start.next.next)
        start = head
        helper(start)


class Solution2:
    def swapPairs(self, head:ListNode) -> ListNode:
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next

        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node

if __name__ == '__main__':

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4


    head = node1

    s = Solution2()
    head = s.swapPairs(head)

    while head:
        print(head.val)
        head = head.next





