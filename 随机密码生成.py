#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: yangyuyi
# @E-mail: TaroYoung2000@gmail.com
# @Date:   2019-08-23 21:25:37
# @Last Modified by:   yangyuyi
# @Last Modified time: 2019-08-23 21:34:01

import random

def genpwd(length):
	return random.randint(10**(length-1),(10**length)-1)

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
