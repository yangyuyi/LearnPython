#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: yangyuyi
# @E-mail: TaroYoung2000@gmail.com
# @Date:   2019-08-29 12:05:09
# @Last Modified by:   yangyuyi
# @Last Modified time: 2019-08-29 12:10:32

import time
scale = 50
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()
for i in range(scale+1):
	a = '*' * i
	b = '.' * (scale - i)
	c = (i/scale)*100
	dur = time.perf_counter() - start
	print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
	time.sleep(0.1)
print("\n执行结束".center(scale//2,'-'))