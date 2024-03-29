#_给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。_
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            dummy=ListNode(None)
            ptr=head
            while ptr:
                temp_new=dummy.next
                temp_old=ptr.next
                dummy.next=ptr
                ptr.next=temp_new
                ptr=temp_old
            return dummy.next
