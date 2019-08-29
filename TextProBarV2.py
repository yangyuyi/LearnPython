#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: yangyuyi
# @E-mail: TaroYoung2000@gmail.com
# @Date:   2019-08-29 12:01:39
# @Last Modified by:   yangyuyi
# @Last Modified time: 2019-08-29 12:04:31

import time

for i in range(101):
	print("\r{:^3}".format(i),end="")
	time.sleep(0.1)