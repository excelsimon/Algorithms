#coding:utf-8

#孤立引用环
"""
a = []
b = [a]
a.append(b)
print(a)
print(b)
del a
del b
print(a)
print(b)

"""


#引用计数
"""
from sys import getrefcount
a = [1,2,3]
print(getrefcount(a))
b = [a,a,a]
print(getrefcount(b))
print(getrefcount(a))

"""

#OOP
"""
class bird(object):
    feature = True
    def __init__(self,type):
        self.type = type
class chicken(bird):
    def __init__(self,type,age):
        super(chicken,self).__init__(type)
        self.age = age
    def __getattr__(self, item):
        self.type = item
        if self.type=='adult':
            return True
        else:
            return False
    def __enter__(self):
        self.age +=1
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.age -=1
        return self
    @staticmethod  #静态成员方法，无需self
    def say():
        print("staticmethod say")
    @classmethod   #类成员方法，self->cls
    def cls_say(cls):
        print("classmethod say")


chicken.say()
chicken.cls_say()
chi = chicken('young',30)
chi.cls_say()
"""
"""
#@property
#Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student(object):
    def __init__(self,birth):
        self.birth = birth

    @property
    def score(self):
        return self._score

    @score.setter   #score可读写
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
    @property    #只定义getter，不定义setter
    def age(self):
        return 2017 - self.birth

s = Student(1990)
s.score = 60 #set
print(s.score) #get
print(s.age)
"""
"""
print(chi.__getattr__('young'))
print(chi.type)
print(getattr(chi,'age'))
print(hasattr(chi,'type'))
print(setattr(chi,'age','年龄'))
print(delattr(chi,'age'))
print(isinstance(chi,chicken))
print(issubclass(chicken,bird))
"""


#对象属性
"""
print(bird.__dict__)
print(chicken.__dict__)
print(chi.__dict__)

{'__dict__': <attribute '__dict__' of 'bird' objects>, '__doc__': None, '__weakref__': <attribute '__weakref__' of 'bird' objects>, '__module__': '__main__', 'feature': True, '__init__': <function bird.__init__ at 0x0000000000BB6598>}
{'__doc__': None, '__init__': <function chicken.__init__ at 0x0000000000BB6620>, '__module__': '__main__', '__getattr__': <function chicken.__getattr__ at 0x0000000000BB6950>, '__exit__': <function chicken.__exit__ at 0x0000000000BB6A60>, '__enter__': <function chicken.__enter__ at 0x0000000000BB69D8>}
{'age': 30, 'type': 'young'}



chi.__dict__['age'] = 25
print(chi.__dict__['age'])
print(chi.age)
chi.age = 20
print(chi.age)

class num(object):
    def __init__(self,value):
        self.value = value
    def getneg(self):
        return -self.value
    def setneg(self,value):
        self.value = -value
    def delneg(self):
        print("value also deleted")
        del self.value
    neg = property(getneg,setneg,delneg,"I'm negative")

x = num(1.1)
print(x.neg)
x.neg = -22
print(x.value)
print(num.neg.__doc__)
del x.neg
"""
#对象引用对象
"""
class from_object(object):
    def __init__(self,to_object):
        self.to_object = to_object
a = [1,2,3]
b = from_object(a)
print(id(a))
print(id(b.to_object))
c = a
print(id(c))
c[0] = 4
print(a)
d = a[:]
d[0]=5
print(d)
print(a)
"""





# #上下文管理器
# class Vow(object):
#     def __init__(self,text):
#         self.text = text
#     def __enter__(self):
#         self.text = "enter " + self.text
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.text = self.text + " exit"
#         return self
#
# mywow = Vow("hello")
# print(mywow.text)
# with Vow("ok") as mywow:
#     print(mywow.text)
# print(mywow.text)

#
# #无参数函数装饰器
#
# def deco(func):
#     def new_func(a,b):
#         print("input",a,b)
#         return func(a,b)
#     return new_func
#
# @deco
# def sum(a,b):
#     return a+b
#
# print(sum(3,4))
# #如果装饰器本身需要支持参数，那么装饰器就需要多一层的内嵌函数
# def deco_with_parameter(pre=''):
#     def _deco(func):
#         def new_func(a,b):
#             print(pre+" input",a,b)
#             return func(a,b)
#         return new_func
#     return _deco
#
# @deco_with_parameter("+")
# def sum_1(a,b):
#     return a+b
#
# print(sum_1(3,4))

#特殊方法
"""
class A(object):
    def __call__(self, a):
        return a+10


a = A()
print(a(20))
lists = list(map(a,[2,3,4]))
print(lists)
"""


#迭代器 可以用for语句循环的对象就是可迭代对象，tuple,list,set,dict,string,
#创建迭代器，为class添加__iter__ __next__  上下文管理器 添加__enter__ __exit__

# class Container(object):
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start<self.end:
#             i = self.start
#             self.start += 1
#             return i
#         else:
#             raise StopIteration("out of range")
#
# c = Container(1,6)
# print(c.__next__())
# print(c.__next__())
# for i in c:
#     print(i)
# print(type(c))

"""
1
2 #for接前面的输出继续输出
3
4
5

"""

# #生成器
# def gen():
#     a = 10
#     yield a
#     a +=1
#     yield a
#
# a = gen()
# for i in a:
#     print(i)
# for i in range(3):
#     print(a.__next__())
#
# """
# 10 11  StopIteration
# """

#print(type(enumerate([1,2,3])))
#<class 'enumerate'>

# #使用迭代器创建生成器
# def generator(start,end):
#     while(start<end):  #访问不到end
#         yield start
#         start +=1
#
# gen = generator(6,10)
# print(type(gen))
# print(gen.__next__())
# for i in gen:
#     print(i)
#
# "<class 'generator'> 6 7 8 9"

# #闭包
# def line_conf():
#     b = 15
#     def line(x):
#         return 2*x + b
#     return line   #返回函数对象
#
# b = 5
# my_line = line_conf()
# #print(my_line.__closure__)
# #print(my_line.__closure__[0].cell_contents)
# print(my_line(b))
# #类装饰器
#
# def decorator(aClass):
#     class new_class():
#         def __init__(self,age):
#             self.total_display = 0
#             self.wrapped = aClass(age)
#
#         def display(self):
#             self.total_display += 1
#             print("total_display:",self.total_display)
#             self.wrapped.display()
#     return new_class
#
# @decorator
# class Bird():
#     def __init__(self,age):
#         self.age = age
#     def display(self):
#         print("My age is:",self.age)
#
# eagle = Bird(5)
# for i in range(3):
#     eagle.display()


#接收多个参数
def func(*args,**kwargs):
    print(type(args))
    print(type(kwargs))
    for i in args:
        print(type(i))
        print(i)
    for k,v in kwargs.items():
        print(type(k))
        print(k,":",v)

func(1,2,3,a=4,b=6)
func({'a':3})
"""
<class 'tuple'>
<class 'dict'>
<class 'int'>
1
<class 'int'>
2
<class 'int'>
3
<class 'str'>
b : 6
<class 'str'>
a : 4
<class 'tuple'>
<class 'dict'>
<class 'dict'>
{'a': 3}
"""











