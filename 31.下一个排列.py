"""
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须 原地 修改，只允许使用额外常数空间。

 

示例 1：

输入：nums = [1,2,3]
输出：[1,3,2]
示例 2：

输入：nums = [3,2,1]
输出：[1,2,3]
示例 3：

输入：nums = [1,1,5]
输出：[1,5,1]
示例 4：

输入：nums = [1]
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
从最后一位往前看，如果比前面的数大，与比数大的最小的数交换顺序，后面的数升序添加到后面即可，如果比它小继续往前找
"""
class Solution:
    def nextPermutation(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums)<=1:
            return nums
        i = len(nums) - 1
        while i>=0:
            if nums[-1]>nums[i]:
                k=len(nums)-2
                while nums[k]>nums[i]:
                    k-=1
                nums[k+1],nums[i] = nums[i],nums[k+1]
                return nums
            else:
                t = nums[i]
                nums[i:-1]=nums[i+1:]
                nums[-1]=t
            i-=1
        return nums
