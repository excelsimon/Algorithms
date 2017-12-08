#coding:utf-8


## top指向list最后一个元素
class Stack(object):
    def __init__(self,size):
        self.top = -1
        self.stack = []
        self.size = size

    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    def isFull(self):
        if self.top+1==self.size:
            return True
        else:
            return False

    def getSize(self):
        return self.top+1

    def push(self,value):
        if self.isFull():
            raise ValueError("The stack is full!")
        self.top+=1
        self.stack.insert(self.top,value)
    def pop(self):
        if self.isEmpty():
            raise ValueError("The stack is empty!")
        else:
            data = self.stack.pop()
            self.top-=1
            return data


if __name__ == '__main__':
    stack1 = Stack(5)
    print("The max size of stack1 is %d:" % (stack1.size,))
    print('before push,stack is empty?',stack1.isEmpty())
    print("before push,stack's top is:",stack1.top)
    try:
        for i in range(10):
            stack1.push(i)
            print('push %d' % (i,))
    except:
        print("stack is full!")
    print('After push %d times,stack is full?' % (i,),stack1.isFull())
    print("After push %d times,stack's top is %d" % (i,stack1.top))
    print('The size of stack1 now is ',stack1.getSize())

    try:
        for i in range(10):
            print(stack1.pop()," pop")
    except:
        print("stack is empty!")

    print("After pop %d times,stack is empty?" % (i,), stack1.isEmpty())
    print("After pop %d times,stack's top is %d" % (i,stack1.top))
    print('The size of stack1 now is ', stack1.getSize())















