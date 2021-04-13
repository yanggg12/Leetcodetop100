"""
6. Z 字形变换
难度
中等

1105





将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);


示例 1：

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
示例 3：

输入：s = "A", numRows = 1
输出："A"


提示：

1 <= s.length <= 1000
s 由英文字母（小写和大写）、',' 和 '.' 组成
1 <= numRows <= 1000
"""
"""
解题思路：
计算每一行的相邻元素的递增思路
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        new_s =''
        length = len(s)
        i = 1
        tmp_idx = i
        j = 1
        while len(new_s)<length:
            new_s += s[tmp_idx-1]
            # old_id = tmp_idx
            if numRows==1:
                return s
            if i == 1 or i == numRows:
                tmp_idx = tmp_idx + 2 * (numRows - 1)
            else:
                if j % 2 != 0:#列向
                    # print("$$$$$$$$$$$$",i)
                    tmp_idx=tmp_idx + 2*(numRows-i)
                else:
                    # print("777777777777777")
                    tmp_idx += 2*(i-1)
            # print(i,j,s[old_id])
            j+=1
            if tmp_idx > length:
                i+=1
                tmp_idx=i
                j=1

        return new_s