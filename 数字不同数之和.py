#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: yangyuyi
# @E-mail: TaroYoung2000@gmail.com
# @Date:   2019-08-23 21:56:42
# @Last Modified by:   yangyuyi
# @Last Modified time: 2019-08-23 21:58:17

str=input()
a=set(str)
print(a)
sum=0
for i in a:
    sum+=eval(i)
print(sum)