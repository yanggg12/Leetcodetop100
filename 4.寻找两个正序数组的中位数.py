"""
4. 寻找两个正序数组的中位数
难度
困难

3630





给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？



示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000


提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
通过次数324,849提交次数822,295
"""
from decimal import Decimal
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        同时从左到右，从右到左遍历两个数组
        1、左边小的一个删除，右边大的一个删除，最后留下一个数或者两个数
        2、退出循环条件，当只剩下一个数或者两个数为止
        :param nums1:
        :param nums2:
        :return:
        """
        n = len(nums1) + len(nums2)
        while n > 2:
            # 删除小的数组第一个数
            if nums1 and nums2:
                if nums1[0] < nums2[0]:
                    nums1.pop(0)
                else:
                    nums2.pop(0)
            elif nums1 and not nums2:
                nums1.pop(0)
            elif nums2 and not nums1:
                nums2.pop(0)
            # 删除大的数组最后一个数
            if nums1 and nums2:
                if nums1[-1] > nums2[-1]:
                    nums1.pop(-1)
                else:
                    nums2.pop(-1)
            elif nums1 and not nums2:
                nums1.pop(-1)
            elif nums2 and not nums1:
                nums2.pop(-1)
            n-=2

        nums3 = nums2+nums1
        if len(nums3) == 1:
            return Decimal(nums3[0]).quantize(Decimal('0.00000'))
        else:
            return  Decimal(sum(nums3) / 2).quantize(Decimal('0.00000'))