#coding:utf8

"""
给定一个数组，找到从1开始，不在数组中的正整数
算法思想：
将找到的元素放到正确的位置上，即将正整数i+1放到array[i]
如果最终发现某个元素一直没有找到则该元素即为所求
算法实际上是在重新填充array

** array[i] == i+1 说明i+1这个正整数放到了正确的位置,继续填充array[i+1]
** array[i] < i+1 第i个位置应该放i+1,但现在小于i+1,array[i]这个整数应该放在前面的位置，前面已经放置妥当，故应删除
** array[i] > size  长度为size的数组最多只能放size个正整数  故应删除
** 假定array[i]=k，i+1 < k < size k应该放在第k-1个位置 交换 array[i]=array[k-1] array[k-1] = k
** 假定array[i]=k，i+1 < k < size 且array[i]=array[k-1] 无需交换，删除array[i]
"""

def first_miss_number(array):
    size = len(array)
    i = 0
    while i<size:
        if array[i] == i+1: #正整数放到了正确的位置
            i += 1
        elif array[i]<i+1 or array[i]>size or array[i]==array[array[i]-1]:
            array[i]=array[size-1]
            size -=1
        else:
            k = array[i]
            array[i] = array[k-1]
            array[k-1] = k

    return i+1

if __name__ == "__main__":
    array = [3,5,1,2,-3,7,4,8]
    m = first_miss_number(array)
    print m