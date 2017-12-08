#coding:utf-8

class Node(object):
    def __init__(self,data,p_next=None):
        self.data = data
        self.p_next = p_next

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)

class SingleLinkedList(object):
    def __init__(self):
        #带头结点
        self.head = Node(0)
        self.length = 0

    #判断链表是否为空
    def isEmpty(self):
        if self.length==0:
            return True
        else:
            return False

    #在链尾增加节点
    def append(self,data):
        item = None
        if isinstance(data,Node):
            item = data
        else:
            item = Node(data)

        node = self.head

        while node.p_next:
            node = node.p_next

        node.p_next = item
        self.length += 1

    #删除一个节点根据值删除 长度记得减1
    def deleteByData(self,data):
        if self.isEmpty():
            raise ValueError("The linkedlist is empty")

        node = self.head
        while node.p_next:
            pre = node
            node = node.p_next
            if node.data == data:
                pre.p_next = node.p_next
                self.length -= 1
                break


    #根据索引删除节点  0 1 2 3 ... length-1
    def deleteByIndex(self,index):
        if index<0 or index>self.length-1 or self.isEmpty():
            raise Exception("out of range")

        node = self.head
        num = -1
        while node.p_next:
            pre = node
            node = node.p_next
            num += 1
            if index == num:
                pre.p_next = node.p_next
                self.length -= 1
                break


    #根据索引更新节点
    def update(self,index,value):
        if index<0 or index>self.length-1 or self.isEmpty():
            raise Exception("out of range")

        node = self.head
        num = -1
        while node.p_next:
            node = node.p_next
            num += 1
            if index == num:
                node.data = value
                break


    #根据索引查找一个节点，返回节点值
    def getItem(self,index):
        if index<0 or index>self.length-1 or self.isEmpty():
            raise Exception("out of range")

        node = self.head
        num = -1
        while node.p_next:
            node = node.p_next
            num += 1
            if index == num:
                return node.data


    #给定某个数据，查找其索引
    def getIndex(self,data):
        if self.isEmpty():
            raise Exception("out of range")

        node = self.head
        num = -1
        while node.p_next:
            node = node.p_next
            num+=1
            if node.data==data:
                return num

    #根据索引插入一个几点

    def insert(self,index,dataOrNode):
        if index < 0 or index > self.length:
            raise Exception("out of range")

        item = None
        if isinstance(dataOrNode,Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if index==0:
            item.p_next=self.head.p_next
            self.head.p_next=item
            self.length+=1
            return



        node = self.head
        num = -1

        if index<self.length:
            while node.p_next:
                pre = node
                node = node.p_next
                num+=1 #num对应node的索引
                if num == index:
                    pre.p_next = item
                    item.p_next = node
                    self.length+=1
                    break
        else:#链表尾部
            while node.p_next:
                node = node.p_next
            node.p_next=item
            self.length+=1


    #清空链表
    def clear(self):
        self.head.p_next=None
        self.length=0


    #显示链表所有节点值

    def __repr__(self):
        node = self.head
        display = []
        while node.p_next:
            node = node.p_next
            display.append(str(node.data))

        return '\t'.join(display)


"""
Test
In [3]: sll = SingleLinkedList()

In [4]: for i in range(5):
   ...:     sll.append(i*i)
   ...:

In [5]: sll
Out[5]: 0       1       4       9       16

In [6]: sll.insert(0,99)

In [7]: sll.insert(6,111)

In [8]: sll
Out[8]: 99      0       1       4       9       16      111

In [9]: sll.length
Out[9]: 7

In [10]: sll.insert(3,Node(33))

In [11]: sll
Out[11]: 99     0       1       33      4       9       16      111

In [12]: sll.length
Out[12]: 8

In [13]: sll.deleteB
sll.deleteByData  sll.deleteByIndex

In [13]: sll.deleteByData(111)

In [14]: sll
Out[14]: 99     0       1       33      4       9       16

In [15]: sll.deleteByData(555)

In [16]: sll
Out[16]: 99     0       1       33      4       9       16

In [17]: sll.deleteByIndex(555)
---------------------------------------------------------------------------
Exception                                 Traceback (most recent call last)
<ipython-input-17-0a60ecf33697> in <module>()
----> 1 sll.deleteByIndex(555)

D:\gitlab\Algorithms\LinkedList.py in deleteByIndex(self, index)
     59     def deleteByIndex(self,index):
     60         if index<0 or index>self.length-1 or self.isEmpty():
---> 61             raise Exception("out of range")
     62
     63         node = self.head

Exception: out of range

In [18]: sll.deleteByIndex(3)

In [19]: sll
Out[19]: 99     0       1       4       9       16

In [20]: sll.length
Out[20]: 6

In [21]: sll.update(0,111)

In [22]: sll
Out[22]: 111    0       1       4       9       16

In [23]: sll.getItem(0)
Out[23]: 111

In [24]: sll.getItem(6)
---------------------------------------------------------------------------
Exception                                 Traceback (most recent call last)
<ipython-input-24-389d070b6c1a> in <module>()
----> 1 sll.getItem(6)

D:\gitlab\Algorithms\LinkedList.py in getItem(self, index)
     91     def getItem(self,index):
     92         if index<0 or index>self.length-1 or self.isEmpty():
---> 93             raise Exception("out of range")
     94
     95         node = self.head

Exception: out of range

In [25]: sll.getItem(5)
Out[25]: 16

In [26]: sll.getIndex(3)

In [27]: sll
Out[27]: 111    0       1       4       9       16

In [28]: print sll.getIndex(3)
None

In [29]: print sll.getIndex(111)
0

"""























