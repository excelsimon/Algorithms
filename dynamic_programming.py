#coding:utf-8

#一、爬楼梯，每次能爬一步或两步，爬十阶楼梯有多少种方法
#1、递归   自顶向下 F(n)=F(n-1)+F(n-2)  F(1)=1  F(2)=2
#时间复杂度，是一颗高度为n的树 o(2^n),空间复杂度为o(1)

def climb_stair_recursive(n):
    if n<0:
        raise ValueError("参数需大于0")
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        return climb_stair_recursive(n-1)+climb_stair_recursive(n-2)


#2、备忘录 自顶向下 但保留了中间计算结果，因为重复计算
#时间复杂度o(n),空间复杂度o(n)

def climb_stair_memo(n):
    dict = {}
    if n<0:
        raise ValueError("参数需大于0")
    if n==1:
        return 1
    if n==2:
        return 2

    if n in dict:
        return dict[n]
    else:
        dict[n] = climb_stair_memo(n-1)+climb_stair_memo(n-2)
        return dict[n]

#3、动态规划
#自底向上 时间复杂度o(n),空间复杂度o(1)

def climb_stair_dynamic(n):
    if n<0:
        raise ValueError("参数需大于0")
    if n==1:
        return 1
    if n==2:
        return 2
    a=1
    b=2
    for i in range(3,n+1):
       tmp = a+b
       a = b
       b = tmp

    return tmp

print climb_stair_recursive(10)
print climb_stair_memo(10)
print climb_stair_dynamic(10)


#二、挖金矿问题
#n座金矿，w个工人，第n座金矿产出黄金g[n-1],需要工人p[n-1]，金矿要么挖要么不挖，求最多能挖多少
# F(n,w)表示n座金矿，w个工人挖最多挖出的金子数目
# 1、金矿数n<=1,工人数w<p[0]，人数不够，挖出黄金数为0  F(n,w)=0 n<=1 w<p[0]
# 2、金矿数n==1,工人数w>=p[0],人数够，只有一座金矿，挖出黄金g[0] F(n,w)=g[0] n==1 w>=p[0]
# 3、金矿编号，从最后一座金矿考虑，如果工人数w小于第n座金矿需要的人数即w<p[n-1],则
# F(n,w)=F(n-1,w) w<p[n-1]
# 4、如果工人数w大于等于第n座金矿需要的人数即w>=p[n-1],第n座金矿有挖与不挖两种情况,最后挖出的黄金数为两种情况中较大的
# 如果挖 挖出黄金g[n-1],剩余金矿n-1座，剩余工人w-p[n-1]   F(n,w)=g[n-1]+F(n-1,w-p[n-1])
# 如果不挖则挖n-1座金矿,工人数还是w个 F(n,w)=F(n-1,w)
# 综合一下 F(n,w)=max(F(n-1,w),g[n-1]+F(n-1,w-p[n-1]))

def gold_dynamic(n,w,g,p):
    pre_results = []
    results = []
    for i in range(w+1):
        pre_results.append(0)
        results.append(0)

    #填充第一行 一座金矿，如果有1个工人，两个工人。。。。w个工人，能挖出的黄金数目,
    #结果存放在pre_results,pre_results[i]表示有i+1个工人1座金矿，能挖出的黄金数
    for i in range(1,w+1):
        if i<p[0]:
            pre_results[i]=0
        else:
            pre_results[i]=g[0]

    #如果只有一座金矿
    if n==1:
        return pre_results[w]

    print pre_results
    #遍历金矿（超过一座），遍历工人
    for gold_num in range(2,n+1):
        for worker_num in range(1,w+1):
            if worker_num<p[gold_num-1]:
                results[worker_num] = pre_results[worker_num]
            else:
                results[worker_num] = max(pre_results[worker_num],g[gold_num-1]+pre_results[worker_num-p[gold_num-1]])
        #浅拷贝害死人
        #pre_results = results
        pre_results = results[:]

        print pre_results

    return results[w]



def max(a,b):
    if a<b:
        return b
    else:
        return a


n = 5
w = 10
p = [5,5,3,4,3]
g = [400,500,200,300,350]

print gold_dynamic(n,w,g,p)

























