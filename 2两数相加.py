"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以
示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# author :yanggx
# time :20210106
# *- encoding=utf-8 -*
'''
1、设置新的数组tmp，
2、遍历两个两个数的结点，相加,大于等于10则向前进一位

'''
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_link(_list):
    result_node = ListNode(_list[0])
    node_tmp = result_node
    for i in range(1, len(_list)):
        node_tmp.next = ListNode(_list[i])
        node_tmp = node_tmp.next
    return result_node

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_node = ListNode(0)
        temp = result_node
        while l1 or l2:
            if l1:
                temp.val = l1.val+temp.val
                l1 = l1.next
            if l2:
                temp.val = l2.val+temp.val
                l2=l2.next
            if temp.val>=10:
                temp.val = temp.val -10
                temp.next = ListNode(1)
                temp = temp.next
            elif l1 or l2:
                temp.next = ListNode(0)
                temp = temp.next
        return result_node


if __name__ == '__main__':
    l1 = list_to_link([2, 4, 3])
    l2 = list_to_link([5, 6, 4])
    ans = Solution().addTwoNumbers(l1, l2)

