from typing import List
import math
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_link(_list):
    result_node = ListNode(_list[0])
    node_tmp = result_node
    for i in range(1, len(_list)):
        node_tmp.next = ListNode(_list[i])
        node_tmp = node_tmp.next
    return result_node


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    def build(_preorder, pre_left, pre_right, _inorder, in_left, in_right):
        if pre_left > pre_right or in_left > in_right:
            return
        # # 下面的判断可以节省一次递归，但是不加不影响最终结果
        # if pre_left == pre_right:
        #     return TreeNode(preorder[pre_left])
        # 前序的第一个结点一定是当前子树的根结点
        tmp_root_data = _preorder[pre_left]
        root = TreeNode(tmp_root_data)
        # 查找结点在中序的位置，可以使用哈希表优化查找
        in_root_idx = _inorder.index(tmp_root_data)
        root.left = build(_preorder, pre_left + 1, pre_left + in_root_idx - in_left, _inorder, in_left,
                          in_root_idx - 1)
        root.right = build(_preorder, pre_left + in_root_idx - in_left + 1, pre_right, _inorder, in_root_idx + 1,
                           in_right)
        return root

    return build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


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




        # """
        # 以一个链表为基准，将另一个链表的一段插入到该链表
        # :param l1:
        # :param l2:
        # :return:
        # """
        # p_l1 = l1
        # head= ListNode()
        # head.next = l1
        # while l2 and p_l1:
        #     p_l2 = l2
        #     while p_l2 and p_l1 and p_l2.val>=p_l1.next.val:
        #         print("22222",p_l2.val,p_l1.val)
        #         p_l1=p_l1.next
        #     print("qqqqqq",  p_l1.val,p_l2.val)
        #     while p_l2 and p_l1.next and p_l2.val <= p_l1.next.val:
        #         print("444", p_l1.val,p_l2.val, p_l1.next.val)
        #         #找到l2中比l1相邻数的子串
        #         if p_l2.next and p_l2.next.val <= p_l1.next.val:
        #             p_l2 = p_l2.next
        #         else:
        #             break
        #
        #     if p_l1.next:
        #         pnext = p_l1.next
        #         p_l1.next = l2
        #         l2 = p_l2.next
        #         p_l2.next = pnext
        #         p_l1=pnext
        #     elif l2:
        #         p_l1.next = l2
        #         break
        # return head.next





l1 = [1,2,4]
l2 = [1,3,4]
l = list_to_link(l1)
l2=list_to_link(l2)

# height =[2,3,10,5,7,8,9]
# # # nums1 = [1, 3]
# # # nums2 = [2]
ans = Solution().mergeTwoLists(l,l2)
while ans:
    print("22222222",ans.val)
    ans=ans.next
# print(ans)
# print(ord("A"))