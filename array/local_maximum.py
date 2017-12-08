#coding:utf8
"""
给定一个无重复元素的数组，求一个该数组的局部最大值
**只需找到一个
**要求数组元素不重复
**局部最大值a[i]满足 a[i-1] < a[i] < a[i],不妨认为a[0]>a[-1] a[N-1]>a[N] 实际上a[-1] a[N]是越界的
如果递增，输出a[N-1],如果递减，输出a[0]
**本质为二分查找


"""

def local_maximum(array):
    len_array = len(array)
    begin = 0
    end = len_array-1

    while(begin<end):
        mid = (begin+end)/2
        # 由于begin<end mid = (begin+end)/2 所以mid+1<=end 不会越界
        if array[mid]>array[mid+1]:
            end = mid
        else:
            begin = mid+1
    return array[begin]

if __name__ == "__main__":
    #array = [1,3,5,9,7,4,10,6]
    #array = [1,3,5,7,9,11]
    array = [7,5,3,1]
    localMax = local_maximum(array)
    print(localMax)