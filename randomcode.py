#-*- coding:utf-8 -*-

'''生成随机码'''

import random
import string


# nums:生成随机码的数量
# bits:生成随机码的位数


def create_randomcode(nums, bits):
    lst = []
    choicelist = string.letters + string.digits
    count = 0
    while count < nums:
        strcode = "".join([random.choice(choicelist) for c in range(8)])
        if strcode not in lst:
            lst.append(strcode)
            count += 1
            print(strcode)
        else:
            continue


if __name__ == '__main__':
    create_randomcode(100, 8)
