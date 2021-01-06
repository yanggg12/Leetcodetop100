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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # len_max = max([len(l1),len(l2)])
        # temp = [0 for i in range(len_max+1)]
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


l1 = list_to_link([2,4,3])
l2 = list_to_link([5,6,4])
ans = Solution().addTwoNumbers(l1,l2)
print(ans)
# print(_input)
pass

