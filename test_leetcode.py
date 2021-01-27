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

class LinkNode:
    __slots__ = ['key','value','prev','next']
    def __init__(self):
        self.key =0
        self.value=0


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity= capacity
        self.head = LinkNode() #头结点
        self.tail = LinkNode() #尾结点
        self.tail.key=-1
        self.head.next,self.tail.prev = self.tail,self.head
        self._map = {} # key到结点的映射


    def get(self, key: int) -> int:
        if key not in self._map:
            return -1
        #将结点移动到最后一位
        self.move_to_end(self._map[key])
        return self._map[key].value


    def put(self, key: int, value: int) -> None:
        if key in self._map:
            self._map[key].value = value
            self.move_to_end(self._map[key])
        else:
            node = self.add_to_end(key,value) #添加到链尾
            self._map[key] = node#添加新结点到映射
            #超过容量，删除第一个结点
            if len(self._map) > self.capacity:
                # print(self._map)
                self._map.pop(self.head.next.key)
                self.delete_first(self.head.next)

                pass

    def move_to_end(self,node:LinkNode)->None:
        #将结点移动到队尾
        node.prev.next, node.next.prev= node.next,node.prev
        node.prev,self.tail.prev.next = self.tail.prev,node
        node.next,self.tail.prev = self.tail,node
    def add_to_end(self,key,value)->LinkNode:
        node = LinkNode()
        node.value = value
        node.key = key
        node.prev,node.next=self.tail.prev,self.tail
        self.tail.prev, node.prev.next =node,node
        return node
    def delete_first(self,node:LinkNode)->None:
        #删除对应的结点
        node.next.prev = node.prev
        node.prev.next =node.next
    # def removenode(self,node:LinkNode)->None:
    #     """
    #     移除结点
    #     :param node:
    #     :return:
    #     """
    #     node.prev, node.next = self.tail.prev, self.tail
    # def add2head(self,node:LinkNode)->None:
    #     """
    #     在头部添加结点
    #     :param node:
    #     :return:
    #     """
    #     node.prev = self.head
    #     node.next = self.head.next
    #     self.head.next.prev = node
    #     self.head.next = node
    # def movetohead(self,node:LinkNode)->None:
    #     self.removenode(node)
    #     self.add2head(node)











# Your LRUCache object will be instantiated and called as such:
lRUCache=LRUCache(2)
lRUCache.put(2, 1)# 缓存是 {1=1}
lRUCache.put(1, 1)# 缓存是 {1=1}
lRUCache.put(2, 3)# 缓存是 {1=1}
lRUCache.put(4, 1)# 缓存是 {1=1}
y=lRUCache.get(1)
y=lRUCache.get(2)   # 返回 1
node = lRUCache.head.next
while node.value!=0:
    print(node.prev.key,node.key,node.next.key)
    node=node.next

print(lRUCache._map)


# l1 = list_to_link([2,4,3])
# l2 = list_to_link([5,6,4])
# s = "abba"
# ans = Solution().lengthOfLongestSubstring(s)
# print(ans)
# # print(_input)
# s=int()
# pass

