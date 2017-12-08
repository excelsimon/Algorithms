#coding:utf-8
"""
基本思想：
1）选择一个基准元素,通常选择第一个元素或者最后一个元素,
2）通过一趟排序讲待排序的记录分割成独立的两部分，其中一部分记录的元素值均比基准元素值小。另一部分记录的 元素值比基准值大。
3）此时基准元素在其排好序后的正确位置
4）然后分别对这两部分记录用同样的方法继续进行排序，直到整个序列有序。

快速排序是通常被认为在同数量级（O(nlog2n)）的排序方法中平均性能最好的。但若初始序列按关键码有序或基本有序时，快排序反而蜕化为冒泡排序。
为改进之，通常以“三者取中法”来选取基准记录，即将排序区间的两个端点与中点三个记录关键码居中的调整为支点记录。快速排序是一个不稳定的排序方法。
"""

import numpy as np
def get_randomint(num):
    i = 0
    lists = []
    while i<num:
        lists.append(np.random.randint(0,100))
        i+=1
    return lists

#递归实现
def quick_sort_recursive(lists,low,high):
    if low>=high:
        return lists
    left = low
    right = high
    key = left

    while left<right:
        while left<right and lists[right]>=lists[key]:
            right-=1
        while left<right and lists[left]<=lists[key]:
            left+=1
        if left<right:
            lists[left],lists[right] = lists[right],lists[left]

    lists[key],lists[right] = lists[right],lists[key]
    quick_sort_recursive(lists,low,left-1)
    quick_sort_recursive(lists,right+1,high)
    return lists

lists = get_randomint(14)
print(lists)
print(quick_sort_recursive(lists,0,len(lists)-1))


#非递归实现

def partition(lists,low,high):
    if low>high:
        return -1
    left = low
    right = high
    key = left

    while left < right:
        while left < right and lists[right] >= lists[key]:
            right -= 1
        while left < right and lists[left] <= lists[key]:
            left += 1
        if left < right:
            lists[left], lists[right] = lists[right], lists[left]

    lists[key], lists[right] = lists[right], lists[key]
    return right

def quick_sort_iterative(lists,low,high):
    stack = []
    stack.append(low)
    stack.append(high)
    while(len(stack)>0):
        right = stack[-1]
        stack.pop()
        left = stack[-1]
        stack.pop()
        key = partition(lists,left,right)
        if key>left+1:
            stack.append(left)
            stack.append(key-1)
        if key<right-1:
            stack.append(key+1)
            stack.append(right)
    return lists

lists_1 = get_randomint(14)
print(lists_1)
print(quick_sort_iterative(lists_1,0,len(lists_1)-1))




























