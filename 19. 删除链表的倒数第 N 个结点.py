# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dumbNode = ListNode(val=None,next=head)
        quick_node =dumbNode
        slow_node =dumbNode
        for i in range(n):
            quick_node=quick_node.next
        while quick_node.next!=None:
            # print(quick_node.val)
            slow_node=slow_node.next
            quick_node=quick_node.next
        # print("dffffffffff")
        # print("dddd",quick_node.val)
        # print(slow_node.val)
        # print(slow_node.next.val)
        slow_node.next = slow_node.next.next
        return dumbNode.next