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
    def convert(self, s: str, numRows: int) -> str:
        new_s =''
        length = len(s)
        i = 1
        tmp_idx = i
        j = 1
        while len(new_s)<length:
            new_s += s[tmp_idx-1]
            # old_id = tmp_idx
            if numRows==1:
                return s
            if i == 1 or i == numRows:
                tmp_idx = tmp_idx + 2 * (numRows - 1)
            else:
                if j % 2 != 0:#列向
                    # print("$$$$$$$$$$$$",i)
                    tmp_idx=tmp_idx + 2*(numRows-i)
                else:
                    # print("777777777777777")
                    tmp_idx += 2*(i-1)
            # print(i,j,s[old_id])
            j+=1
            if tmp_idx > length:
                i+=1
                tmp_idx=i
                j=1

        return new_s



s = "12"
# # nums1 = [1, 3]
# # nums2 = [2]
ans = Solution().convert(s,1)
print(ans)
