"""
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？


示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]


提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109
"""
"""
思路：二分法先找到一个值，然后左右依次搜索
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,len(nums)-1
        if nums[l]>target or nums[r]<target:
            return [-1,-1]
        t = [-1,-1]
        while l<=r:
            mid = (l+r)//2
            print(l,r,mid)
            if nums[mid]==target:
                t=[mid,mid]
                while t[0] - 1 >= 0 and nums[t[0] - 1] == nums[mid]:
                    t[0] -= 1
                print(nums[t[-1] + 1])
                while t[-1] + 1 <= len(nums) - 1 and nums[t[-1] + 1] == nums[mid]:
                    t[-1] += 1
                break
            if nums[l]<=target<nums[mid]:
                r=mid-1
            elif nums[mid]<target<=nums[r]:
                l=mid+1
            else:
                break
            # break
        return t
