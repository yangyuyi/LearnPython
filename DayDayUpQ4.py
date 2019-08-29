#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: yangyuyi
# @E-mail: TaroYoung2000@gmail.com
# @Date:   2019-08-29 00:01:51
# @Last Modified by:   yangyuyi
# @Last Modified time: 2019-08-29 07:18:09
#DayDayUpQ4.py

def dayUp(df):
 	dayup = 1
 	for i in range(365):
 		if i % 7 in [6,0]:
 			dayup *= 1-0.01
 		else:
 			dayup *= 1+df
 	return dayup

dayfactor = 0.01
while dayUp(dayfactor) <37.78:
	dayfactor += 0.001
print("工作日的努力参数是：{:.3f}".format(dayfactor))