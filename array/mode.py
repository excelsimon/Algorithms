#coding:utf8
"""
绝对众数
给定N个数，出现次数最多的为众数，如果某众数出现次数多余N/2，则称为绝对众数
显然，只能有一个绝对众数
算法核心：
    删掉数组中两个不同的数，剩余数组中的绝对众数和之前数组中的绝对众数一样

"""
#要求数组array中有绝对众数
def Mode(array):
    len_array = len(array)
    count = 0
    m = 0 #初始化m，任意值
    for i in xrange(len_array):
        if count == 0:
            m = array[i]
            count = 1
        elif m != array[i]:
            count -= 1
        else: # count!=0 m=array[i]
            count += 1
    return m
"""
给定N个整数，查找出现次数超过N/3的所有可能的数
显然，最多有两个
思路同上，删掉三个不同的数，剩余数组中的N/3绝对众数和之前数组中的绝对众数一样
"""
def Mode_2(array):
    m = 0
    n = 0
    cm = 0
    cn = 0
    result = []
    len_array = len(array)
    for i in range(len_array):
        if cm == 0:
            m = array[i]
            cm = 1
        elif m == array[i]:
            cm +=1
        elif cn == 0:
            n = array[i]
            cn += 1
        elif n == array[i]:
            cn +=1
        else:
            cm -= 1
            cn -= 1

    cm = cn = 0
    for i in range(len_array):
        if array[i] == m:
            cm += 1
        elif array[i] == n:
            cn += 1

    if cm>len_array/3:
        result.append(m)
    if cn>len_array/3:
        result.append(n)

    return result




if __name__ == "__main__":
    array1 = [8,8,1,1,1,8,1,1,6,1,8]
    m = Mode(array1)
    print(m)

    array2 = [2,2,1,3,4,2,2,1,1]
    #array2 = [1,2,3,2,5,2,2,3,3,2,3]
    mode = Mode_2(array2)
    if len(mode)>0:
        print(mode)
    else:
        print("Not Found!")
