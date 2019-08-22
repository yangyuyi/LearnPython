#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: yangyuyi
# @E-mail: TaroYoung2000@gmail.com
# @Date:   2019-08-22 14:56:59
# @Last Modified by:   yangyuyi
# @Last Modified time: 2019-08-22 15:00:47

sum=0
for i in range(2,100):
    for j in range (2,int(i**0.5)+1):
        if (i%j==0):
            break
    else:
        sum+=i
print(sum)