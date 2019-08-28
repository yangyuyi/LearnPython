#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: yangyuyi
# @E-mail: TaroYoung2000@gmail.com
# @Date:   2019-08-28 23:17:10
# @Last Modified by:   yangyuyi
# @Last Modified time: 2019-08-28 23:21:54
#DayDayUpQ3.py

dayup = 1.0
dayfactor = 0.01
for i in range(365):
	if i % 7 in [6,0]:
		dayup = dayup*(1-dayfactor)
	else:
		dayup = dayup*(1+dayfactor)
print("{:.2f}".format(dayup))