#-*- coding:utf-8 -*-

'''猜数小游戏'''

import random


def guess():
    print("游戏开始！")
    print("输入一个1到100的整数，点击回车：")
    right_num = random.choice(range(1, 101))
    count = 0  # 记录猜数次数
    while True:
        try:
            num = int(raw_input())
        except Exception, e:
            print("请输入一个100以内的整数!")
        else:
            count += 1
            if num == right_num:
                print("哇！猜中了！累计用了{0}次".format(count))
                break
            elif num > right_num:
                print("猜大了！累计用了{0}次".format(count))
            else:
                print("猜小了！累计用了{0}次".format(count))
    raw_input()

if __name__ == "__main__":
    guess()
