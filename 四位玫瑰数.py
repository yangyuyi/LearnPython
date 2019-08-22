#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: yangyuyi
# @E-mail: TaroYoung2000@gmail.com
# @Date:   2019-08-22 14:52:41
# @Last Modified by:   yangyuyi
# @Last Modified time: 2019-08-22 14:53:39

for i in range(1000,10000):
    x1=i//1000
    x2=i//100%10
    x3=i//10%10
    x4=i%10
    if (x1**4+x2**4+x3**4+x4**4==i):
        print(i)