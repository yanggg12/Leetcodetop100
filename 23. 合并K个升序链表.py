"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]
 

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res_Listnode = ListNode()
        p_r = res_Listnode
        f=[]
        for i in lists:
            if i:
                f.append(i)
        lists=f
        while lists:
            vals = [tmp_listnode.val for tmp_listnode in lists]
            min_indx = vals.index(min(vals))
            p_r.next = lists[min_indx]
            p_r = lists[min_indx]
            if not lists[min_indx].next:
                lists = [lists[i] for i in range(len(lists)) if i!=min_indx]
            else:
                lists[min_indx] = lists[min_indx].next
            p_r.next =None
        return res_Listnode.next