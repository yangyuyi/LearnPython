#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: yangyuyi
# @E-mail: TaroYoung2000@gmail.com
# @Date:   2019-08-28 23:11:10
# @Last Modified by:   yangyuyi
# @Last Modified time: 2019-08-28 23:16:14
#DayDayUpQ2.py

dayfactor = 0.005
dayup = pow(1+dayfactor,365)
daydown = pow(1-dayfactor,365)
print("向上：{:.2f}向下：{:.2f}".format(dayup,daydown))

dayupup = pow(1+dayfactor*2,365)
daydowndown = pow(1-dayfactor*2,365)
print("向上：{:.2f}向下：{:.2f}".format(dayupup,daydowndown))