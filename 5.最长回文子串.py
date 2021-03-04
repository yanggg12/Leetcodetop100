# author :yanggx
# time :20210303
# *- encoding=utf-8 -*
'''
5. 最长回文子串
难度
中等

3269





给你一个字符串 s，找到 s 中最长的回文子串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"
'''
#中心扩散法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0

        for i in range(len(s)):
            left1, right1 = self.expandAroudcouter(s, i, i)
            left2, right2 = self.expandAroudcouter(s, i, i+1)
            if left1 < right1 and right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]

    def expandAroudcouter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1