#coding:utf-8
"""
字符串查找
在text文本中查找pattern，如果找到则返回第一个字符匹配的位置，否则返回-1
   
"""

#暴力求解
#时间复杂度o(n*m)
def brute_force_search(text,pattern):

    n = len(text)
    m = len(pattern)

    k = 0
    for i in range(n):
        for j in range(i,i+m):
            if text[j] == pattern[k]:
                k+=1
            else:
                k = 0
                break
        if k == m:
            return i

    return -1

#text = "abacdefg"
#pattern1 = "cde"
#pattern2 = "hehe"
#print brute_force_search(text,pattern1)#3
#print brute_force_search(text,pattern2)#-1

#KMP算法
#暴力求解是text逐位移动
#KMP假设在pattern的第j个字符与text不匹配，那么前j-1个字符与text是匹配的
#下次比较的时候，把pattern的前j-1个字符当作一个整体往前滑动
#text: .........pattern[0],pattern[1]...pattern[j-1]..........
#pattern:       pattern[0],pattern[1]...pattern[j-1],pattern[j].........
#可以直观的看到下次要和text进行匹配的位置应该是pattern的前缀串和后缀串相等的位置
#前缀串和后缀串可能有多个相等的情况，需要取最长的那个（这个长度记为k），这样滑动的距离最小，不会遗漏
#patteren[0],pattern[1]...pattern[k-1] == pattern[j-k],pattern[j-k+1]....pattern[j-1]
#用一个next数组记录pattern的每个字符的k值
#求next数组
#pattern[0] 对应next[0]=-1  pattern[1] 对应next[1]=0
#next[j]对应pattern[j]
#求next[j]和next[j+1]的递推关系
#假定next[j]=k
#pattern[0],...pattern[k-1]        ==         pattern[j-k],....pattern[j-1]
#pattern[0],...pattern[k-1],pattern[k]........pattern[j-k],....pattern[j-1],pattern[j]
#如果pattern[j] == pattern[k] 那么next[j+1] = next[j]+1
#如果pattern[j] != pattern[k]
#假定next[k]=h 由于pattern[0],...pattern[k-1] == pattern[j-k],....pattern[j-1]
#pattern[0]..pattern[h-1] == pattern[k-h]..pattern[k-1] == pattern[j-k]..pattern[j-k+h-1] == pattern[j-h]..pattern[j-1]
#pattern[0]..pattern[h-1]....pattern[k-h]..pattern[k-1]....pattern[j-k]..pattern[j-k+h-1]....pattern[j-h]..pattern[j-1],pattern[j]
#如果pattern[j]==pattern[h] 那么next[j+1]=h+1
#如果pattern[j]!=pattern[h]重复上述过程，结束条件是next[h]==0
#求得next数组以后进行匹配，pattern[j]与text不匹配，next[j]=k,则text往前滑动距离为j-k即j-next[j]
##text: .........pattern[0],...pattern[k-1]........pattern[j-k],....pattern[j-1]..........
#pattern:        pattern[0],...pattern[k-1]........pattern[j-k],....pattern[j-1],pattern[j]


def getNext(pattern):
    m = len(pattern)
    next = []
    for j in range(m):
        next.append(0)
    next[0] = -1
    k = next[0]
    i = 1
    #k记录前一个字符最长匹配前后串的长度
    while i<m:
        #只有在匹配到或者k==-1即匹配到第一个字符的时候才填充下一个
        if k==-1 or pattern[i-1]==pattern[k]:
            next[i] = k+1
            k = next[i]
            i+=1
        else:
            k = next[k]
    return next


def max(a,b):
    if a>b:
        return a
    else:
        return b

def kmp(text,pattern):
    next = getNext(pattern)
    n = len(text)
    m = len(pattern)
    if n<m:
        return -1
    i = 0
    while i<=n-m:

        match = True
        for j in range(m):
            if text[i+j] != pattern[j]:
                match = False
                break

        if match:
            return i
        else:
            i += j - next[j]
            #print i

    return -1


if __name__ == "__main__":

    text = "ababcabcdefabcabcebbeab"
    pattern = "abcabce"
    print getNext(pattern)
    print brute_force_search(text,pattern)
    print kmp(text,pattern)




















