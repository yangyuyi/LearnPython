#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: yangyuyi
# @E-mail: TaroYoung2000@gmail.com
# @Date:   2019-08-23 21:45:07
# @Last Modified by:   yangyuyi
# @Last Modified time: 2019-08-23 21:45:37
# 请在...补充一行或多行代码

def prime(m):
    for i in range(2,int(m**0.5)+1):
        if m%i==0:
            return False
    return True
    
n = eval(input())
n_=int(n)
if n_<n:
    n_=n_+1
i=5
while (i>0):
    if prime(n):
        if i>1:
            print(n,end=",")
            i=i-1
        else:
            print(n,end="")
            i=i-1
    n=n+1
