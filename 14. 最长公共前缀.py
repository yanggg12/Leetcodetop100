"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        def two_substr(str1,str2):
            res=''
            i=0
            length_str1,length_str2=len(str1),len(str2)
            while True:
                # print("eeeeeeeeeeeeee",i,length_str1,length_str2,str1[i],str2[i])
                if i <length_str1 and i <length_str2 and str1[i]==str2[i]:
                  # print("ssssssssss",i)
                  res+=str1[i]
                  i+=1
                else:
                    break
            # print(res)
            return res
        str1 = strs[0]
        for sub_str in strs[1:]:
            str1 = two_substr(str1,sub_str)
            if not str1:
                return ''
        return str1
