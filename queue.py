# coding=utf-8


# 构造一个队列的类
class Queue(object):

    def __init__(self, size):
        self._queue = []
        self._size = size
        self._head = -1
        self._tail = -1

    def IsEmpty(self):
        '''判断队列是否为空'''
        if self._head == self._tail:
            return True
        else:
            return False

    def IsFull(self):
        '''判断队列是否为满'''
        if self._tail-self._head == self._size:
            return True
        else:
            return False

    def In(self, str):
        '''进队列操作'''
        if self.IsFull():
            print('队列满')
        else:
            self._queue.append(str)
            self._tail = self._tail+1

    def Out(self):
        if self.IsEmpty():
            print('队列空')
        else:
            del self._queue[0]
            self._head = self._head+1

    def Print(self):
        '''打印队列内元素'''
        for b in self._queue:
            print(b)

    def Count(self):
        '''计算队列内元素数量'''
        print('Count：{0}'.format(self._tail-self._head))
