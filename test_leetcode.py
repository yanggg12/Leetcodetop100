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
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_str_len = 0
        char2idex = {}
        max_chars_start = 0
        max_chars_end = 0
        temp_start = 0
        # temp_end = 0#[temp_end]是字串的最后一个字符索引,多余
        # no_repetition = False #这一步多余，实际上，只需要在遇到无无重复字符的时候计算即可
        for i in range(len(s)):
            if char2idex.get(s[i],-1)>=temp_start:#如果字符在临时串中,则更新临时串
                #与当前最长字符串比较大小
                # temp_len = temp_end - temp_start + 1
                # if max_str_len< temp_len:
                #     max_str_len = temp_len
                    # max_chars_end = temp_end
                    # max_chars_start = temp_start
                temp_start = char2idex.get(s[i])+1
                char2idex[s[i]] = i
                # temp_end = i#多余
            else:
                    char2idex[s[i]] = i
                    # temp_end=i#多余
                    #no_repetition = True
                    max_str_len = max(i - temp_start + 1, max_str_len)#只需要在这一步计算
        # if no_repetition:
        #     temp_len = temp_end - temp_start + 1
        #     max_str_len = max(temp_len,max_str_len)
        return  max_str_len






l1 = list_to_link([2,4,3])
l2 = list_to_link([5,6,4])
s = "abba"
ans = Solution().lengthOfLongestSubstring(s)
print(ans)
# print(_input)
pass

