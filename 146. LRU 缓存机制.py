"""
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：

LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 

进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？

 

示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
 

提示：

1 <= capacity <= 3000
0 <= key <= 3000
0 <= value <= 104
最多调用 3 * 104 次 get 和 put

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
分析：个人难点，记录最久没有使用的关键字，采用队列：关键字被使用则添加到队尾，每次删除队首元素
"""


class LinkNode:
    __slots__ = ['key', 'value', 'prev', 'next']

    def __init__(self):
        self.key = 0
        self.value = 0


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = LinkNode()  # 头结点
        self.tail = LinkNode()  # 尾结点
        self.tail.key = -1
        self.head.next, self.tail.prev = self.tail, self.head
        self._map = {}  # key到结点的映射

    def get(self, key: int) -> int:
        if key not in self._map:
            return -1
        # 将结点移动到最后一位
        self.move_to_end(self._map[key])
        return self._map[key].value

    def put(self, key: int, value: int) -> None:
        if key in self._map:
            self._map[key].value = value
            self.move_to_end(self._map[key])
        else:
            node = self.add_to_end(key, value)  # 添加到链尾
            self._map[key] = node  # 添加新结点到映射
            # 超过容量，删除第一个结点
            if len(self._map) > self.capacity:
                # print(self._map)
                self._map.pop(self.head.next.key)
                self.delete_first(self.head.next)

                pass

    def move_to_end(self, node: LinkNode) -> None:
        # 将结点移动到队尾
        node.prev.next, node.next.prev = node.next, node.prev
        node.prev, self.tail.prev.next = self.tail.prev, node
        node.next, self.tail.prev = self.tail, node

    def add_to_end(self, key, value) -> LinkNode:
        node = LinkNode()
        node.value = value
        node.key = key
        node.prev, node.next = self.tail.prev, self.tail
        self.tail.prev, node.prev.next = node, node
        return node

    def delete_first(self, node: LinkNode) -> None:
        # 删除对应的结点
        node.next.prev = node.prev
        node.prev.next = node.next
