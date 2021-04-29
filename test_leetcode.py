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

_list = [1,2,3,4,5]
l = list_to_link(_list)


# height =[2,3,10,5,7,8,9]
# # # nums1 = [1, 3]
# # # nums2 = [2]
ans = Solution().removeNthFromEnd(l,2)
while ans:
    print(ans.val)
    ans=ans.next
print(ans)
# print(ord("A"))