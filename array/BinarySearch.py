#coding:utf8
"""
折半查找，又称二分查找
要求数组有序
"""

def BiSearch(array,search):
    len_array = len(array)
    begin = 0
    end = len_array-1
    while begin<=end:
        index = (begin + end) / 2
        if array[index]==search:
            return index
        elif array[index]>search:
            end = index-1
        else:
            begin = index+1
    return -1

if __name__ == "__main__":
    array = []
    for i in range(10):
        array.append(i * i)
    search = 81
    index = BiSearch(array, search)
    if index != -1:
        print array[index]
    else:
        print 'Not found!'
