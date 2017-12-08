#coding:utf-8

class Queue(object):
    def __init__(self,size):
        self.size = size
        self.queue = []

    def isEmpty(self):
        if len(self.queue)==0:
            return True
        else:
            return False

    def isFull(self):
        if len(self.queue)==self.size:
            return True
        else:
            return False

    def enqueue(self,value):
        if self.isFull():
            raise ValueError("The queue is full")
        else:
            self.queue.append(value)

    def dequeue(self):
        if self.isEmpty():
            raise ValueError("The queue is empty")
        else:
            front = self.queue[0]
            self.queue.remove(front)
            return front

    def getSize(self):
        return len(self.queue)


if __name__ == '__main__':
    queue1 = Queue(5)
    print('The max size of queue1 is: ',queue1.size)
    print('Before enqueue,the size of queue1 is:',queue1.getSize())
    print('Before enqueue,queue1 is empty?',queue1.isEmpty())
    try:
        for i in range(10):
            print('%d enqueue' % (i,))
            queue1.enqueue(i)
    except:
        print('queue1 is full!')

    print('after %d times enqueue,queue is full' % (i,))

    try:
        for i in range(10):
            print(queue1.dequeue(),'dequeue')
    except:
        print('queue1 is empty!')

    print('after %d times dequeue,queue is empty' % (i,))
