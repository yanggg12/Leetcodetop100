"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]
 

提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
通过次数553,308提交次数839,568

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3=ListNode()
        p3 = l3
        while l1 and l2:
            p1,p2=l1,l2
            while p1.val<=p2.val:
                if p1.next and p1.next.val<=p2.val:
                    p1=p1.next
                else:
                    break
            if p1.val<=p2.val:
                p3.next = l1
                p3=p1
                l1 = p1.next
            while p1.val>p2.val:
                if p2.next and p2.next.val<p1.val:
                    p2=p2.next
                else:
                    break
            if p2.val<p1.val:
                p3.next = l2
                p3=p2
                l2 = p2.next
        if l1:
            p3.next=l1
        elif l2:
            p3.next=l2
        return  l3.next