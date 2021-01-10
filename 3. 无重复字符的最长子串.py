"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
通过次数784,874提交次数2,172,451

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# author :yanggx
# time :20210108
# *- encoding=utf-8 -*
'''
1、要记录已遍历的字符所在的位置，每个位置对应的字符长度，
2、遇到重复的字符a记录到n1之前的片段和长度，第二段起始从与前一个字符a后面开始记录
计算长度只需要在每一增加一个无重复字符的时候计算一次即可
'''
class Solution:
    def lengthOfLongestSubstring_me(self, s: str) -> int:
        """
        自己写的代码，有赘余，已经根据答案简化
        :param s:
        :return:
        """
        max_str_len,temp_start,char2idex = 0,0,{}#最长子串长度，左指针，记录已出现的字符与最新id映射
        for i in range(len(s)):
            if char2idex.get(s[i],-1)>=temp_start:#如果字符在临时串中,则更新临时串
                temp_start = char2idex.get(s[i])+1 #左指针右移一位
                char2idex[s[i]] = i #更新重复字符的最新id为当前位置
            else:
                char2idex[s[i]] = i
                max_str_len = max(i - temp_start + 1, max_str_len)#更新最大子串
        return  max_str_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

"""    作者：LeetCode - Solution
    链接：https: // leetcode - cn.com / problems / longest - substring - without - repeating - characters / solution / wu - zhong - fu - zi - fu - de - zui - chang - zi - chuan - by - leetc - 2 /
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""