#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: yangyuyi
# @E-mail: TaroYoung2000@gmail.com
# @Date:   2019-08-29 11:45:07
# @Last Modified by:   yangyuyi
# @Last Modified time: 2019-08-29 11:52:51

import time
scale = 10
print("------执行开始------")
for i in range(scale+1):
	a = '*' * i
	b = '.' * (scale-i)
	c = (i/scale)*100
	print("{:^3.0f}%[{}->{}]".format(c,a,b))
	time.sleep(0.1)
print("------执行结束------")
