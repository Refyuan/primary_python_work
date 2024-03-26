# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 两个链表的节点数目范围是[0, 50]
# -100 <= Node.val <= 100
# l1和l2均按非递减顺序排列
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        p = dummy
        while list1 and list2:
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next

        if list1:
            p.next = list1
            list1 = list1.next
        else:
            p.next = list2
            list2 = list2.next
        return dummy.next
