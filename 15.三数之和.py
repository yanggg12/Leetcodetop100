"""
15. 三数之和
难度
中等

3295





给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。



示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]


提示：

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 对数组进行排序从小到大
        lens = len(nums)
        self.quick_sort(nums, 0, lens - 1)
        res = []
        i = 0
        j = lens - 1
        if lens >= 3:
            while i < j and nums[i] <= 0 and nums[j] >= 0:
                k = i + 1
                while k < j:
                    # print([nums[i],nums[k],nums[j]])
                    flg = nums[k] + nums[j]
                    if nums[i] + flg == 0 and [nums[i], nums[k], nums[j]] not in res:
                        res.append([nums[i], nums[k], nums[j]])
                        k += 1
                        j -= 1
                    elif nums[i] + flg < 0:
                        k += 1
                    else:
                        j -= 1

                i += 1
                j = lens - 1
        return res

    def quick_sort(self, nums, left, right):
        if left < right:
            i = left
            j = right
            # 取第一个元素为枢轴量
            pivot = nums[left]
            while i != j:
                # 交替扫描和交换
                # 从右往左找到第一个比枢轴量小的元素，交换位置
                while j > i and nums[j] > pivot:
                    j -= 1
                if j > i:
                    # 如果找到了，进行元素交换
                    nums[i] = nums[j]
                    i += 1
                # 从左往右找到第一个比枢轴量大的元素，交换位置
                while i < j and nums[i] < pivot:
                    i += 1
                if i < j:
                    nums[j] = nums[i]
                    j -= 1
            # 至此完成一趟快速排序，枢轴量的位置已经确定好了，就在i位置上（i和j)值相等
            nums[i] = pivot
            # 以i为枢轴进行子序列元素交换
            self.quick_sort(nums, left, i - 1)
            self.quick_sort(nums, i + 1, right)