# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
# 你应当保留两个分区中每个节点的初始相对位置。
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # dummy1=ListNode(None)
        # dummy2=ListNode(None)
        # small_ptr=dummy1
        # big_ptr=dummy2
        # while head:
        #     if head.val<x:
        #         dummy1.next=head
        #         head=head.next
        #         small_ptr=small_ptr.next
        #     else:
        #         dummy2.next=head
        #         head = head.next
        #         big_ptr = big_ptr.next
        # small_ptr.next=dummy2.next
        # return small_ptr
        dummy1 = ListNode(None)
        small_ptr = dummy1
        dummy2 = ListNode(None)
        big_ptr = dummy2
        ptr = head
        while ptr:
            if ptr.val <x:
                small_ptr.next = ptr
                small_ptr = small_ptr.next
            else:
                big_ptr.next = ptr
                big_ptr = big_ptr.next
            temp = ptr.next
            ptr.next = None
            ptr = temp
        small_ptr.next = dummy2.next
        return dummy1.next