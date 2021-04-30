'''
7. 整数反转
难度
简单
2696
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。


示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0


提示：

-231 <= x <= 231 - 1
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        if x < 0:
            flag = -1
        else:
            flag = 1
        x = abs(x)
        while x >= 10:
            a = x % 10
            if res == 0:
                res = res + a
            else:
                res = res * 10 + a
            x = x // 10

        res = flag * (res * 10 + x)

        if res < -2 ** 31 or res > 2 ** 31 - 1:
            return 0
        return res
