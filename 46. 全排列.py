"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

 

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
 

提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
解题思路：枚举法，回溯法
"""

#我的写法
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        import copy
        res = []
        # n=len(nums)
        def helper(tmp_list,n0):
            tmp_res = []
            # print("eeeeee",tmp_list)
            for x in range(len(tmp_list)):
                # print("55555",x,tmp_res,tmp_list)
                tmp_res.append(copy.deepcopy(tmp_list))
                # print("22222222", tmp_res)
                tmp_res[x][x:x+1]=[n0,tmp_list[x]]
                # print("111111",tmp_res)
            tmp_res.append(copy.deepcopy(tmp_list)+[n0])

            return tmp_res
        if  len(nums)==1:
            return [nums]
        elif len(nums)==2:
            return [nums,[nums[-1],nums[0]]]
        else:
            for tmp_list in self.permute(nums[1:]):
                # print(tmp_list)
                # print("dd",res,tmp_list,nums)
                res+=helper(tmp_list, nums[0])
        return res
#d大佬的写法
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            print(tmp, print(nums))
            if not nums:

                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res

    