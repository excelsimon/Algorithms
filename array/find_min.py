#coding:utf8
"""
假定一个排序数组以某个元素为支点做了旋转，如：0 1 2 4 5 6 7 旋转后得到4 5 6 7 0 1 2
找出旋转后数组的最小值，假定数组元素没有重复
本质为二分查找
时间复杂度o(logN)
"""

def find_min(array):
    len_array = len(array)
    low = 0
    high = len_array - 1
    while low<high:
        mid = (low+high)/2
        if array[mid]<array[high]: #最小值在左半部分
            high = mid
        elif array[mid]>array[high]: #最小值在右半部分
            low = mid+1

    return array[low]


if __name__ == "__main__":
    array = [4,5,6,7,0,1,2]
    min = find_min(array)
    print min