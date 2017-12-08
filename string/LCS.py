
#coding:utf-8
import numpy as np

#一、字符串循环左移
"""
给定字符串s[0...N-1],要求把s的前k个字符移到s尾部
如把'abcdef'前两个字符移到尾部得到'cdefab'

ab->ba
cdef->fedc
bafedc->cdefab

"""

def left_rotate_string(s,k):
    if k>len(s):
        raise ValueError("参数太大")

    s1 = s[:k][::-1]
    s2 = s[k:][::-1]
    s3 = s1+s2

    return s3[::-1]

s='abcdef'
k=2
#print left_rotate_string(s,2)


#二、最长公共子序列
"""
Longest common subsequence
一个序列S任意删除若干个字符得到新序列T，则T叫做S的子序列
两个序列X和Y的公共子序列中，长度最长的那个，定义为X和Y的最长公共子序列

1、如果某个字符串长度为0,则LCS(x,y)=''
2、两个字符串最后一位相同,则LCS(x,y) = LCS(x[:-1],y[:-1]) + x[-1](或者y[-1])
3、两个字符串最后一位不同,则LCS(x,y) = max_str(LCS(x[:-1],y[:]),LCS(x[:],y[:-1]))

"""
def max_str(str1,str2):
    if len(str1)>len(str2):
        return str1
    else:
        return str2

def LCS_recursive(x,y):
    if len(x)==0 or len(y)==0:
        return ''

    if x[-1]==y[-1]:
        return LCS_recursive(x[:-1],y[:-1])+x[-1]
    else:
        return max_str(LCS_recursive(x[:-1],y[:]),LCS_recursive(x[:],y[:-1]))

str1 = 'BCDABAB'
str2 = 'CBAABAABA'
print(LCS_recursive(str1,str2))
#CABAB

def max_int(a,b):
    c = (a if a>b else b)
    return c

def LCS_dynamic(x,y):
    x_len = len(x)
    y_len = len(y)
    matrix = []
    result_str = []

    #x_len+1行,y_len+1列的矩阵
    #初始化矩阵
    line = []
    for j in range(y_len + 1):
        line.append(0)

    for i in range(x_len+1):
        matrix.append(line[:])#浅拷贝害死人
    #print len(matrix),len(matrix[0])
    #矩阵零行零列填充完毕，填充矩阵剩余部分，矩阵从0行开始，矩阵第i行对应x[i-1]
    for i in range(1,x_len+1):
        for j in range(1,y_len+1):
            if x[i-1]==y[j-1]:
                #result_str.append(x[i-1])
                matrix[i][j]=matrix[i-1][j-1]+1
            else:
                matrix[i][j]=max_int(matrix[i-1][j],matrix[i][j-1])

    i = x_len
    j = y_len

    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            result_str.append(x[i-1])
            i-=1
            j-=1
        else:
            if matrix[i][j-1]>matrix[i-1][j]: #left>top
                j-=1
            else:
                i-=1
    print np.array(matrix)

    return matrix[x_len][y_len],result_str[::-1]
x='ABCBDAB'
y='BDCABA'
print(LCS_dynamic(x,y))


'''
Test result
[[0 0 0 0 0 0 0]
 [0 0 0 0 1 1 1]
 [0 1 1 1 1 2 2]
 [0 1 1 2 2 2 2]
 [0 1 1 2 2 3 3]
 [0 1 2 2 2 3 3]
 [0 1 2 2 3 3 4]
 [0 1 2 2 3 4 4]]
(4, ['B', 'C', 'B', 'A'])
'''



























