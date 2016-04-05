# coding=utf-8

#构造一个栈的类
class Stack():

    def __init__(self, size):
        self._stack = []
        self._size = size
        self._top = -1

    def IsFull(self):
        '''判断栈内元素是否满了'''
        if self._top+1 == self._size:
            return True
        else:
            return False

    def IsEmpty(self):
        '''判断栈是否为空'''
        if self._top == -1:
            return True
        else:
            return False

    def Push(self, str):
        '''入栈操作'''
        if self.IsFull():
            print('栈满了')
        else:
            self._stack.append(str)
            self._top = self._top+1

    def Pop(self):
        '''出栈操作'''
        if self.IsEmpty():
            print('栈为空')
        else:
            del self._stack[self._top]
            self._top = self._top-1

    def Print(self):
        '''打印栈内元素'''
        for a in self._stack:
            print(a)

    def Count(self):
        '''计算栈内元素数量'''
        print('Count：{0}'.format(self._top+1))
