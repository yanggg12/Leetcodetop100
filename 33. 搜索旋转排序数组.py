"""
33. 搜索旋转排序数组
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：

输入：nums = [1], target = 0
输出：-1
"""

"""
解题思路：使用二分法
1.比较与首位两数的大小：
   if Xn-1<target<X0 :return -1
   else:
   取X[n/2]
   if target=X[n/2] return [n/2]
   elif target >X0: 循环二分法找到比target大的第一个数，然后用二分法查找
   if Xn-1>target:循环二分法找到比target小的第一个数，然后用二分法查找
"""


def dichotomy(X, target):
    """

    :param X: list 数组
    :param target: 目标值
    :return: -1，没有搜索到target,int>=0target所在索引
    """
    # 反复取中间的数直到target==中间的数或者区间为空，返回编号
    X0,X1=0,len(X)-1
    if target == X[X0]:
        return X0
    elif target == X[X1]:
        return X1
    if not X:
        return -1
    while X0 <= X1:
        mid = (X0 + X1 )//2
        if target == X[mid]:
            return mid
        if X[0] <= X[mid]:
            if X[0] <= target < X[mid]:
                X1 = mid - 1
            else:
                X0 = mid + 1
        else:
            if X[mid] < target <= X[-1]:
                X0 = mid + 1
            else:
                X1 = mid - 1
    return -1


target = 0
X = [4, 5, 6, 7, 0, 1, 2]
s = dichotomy(X,target)
print(s)
