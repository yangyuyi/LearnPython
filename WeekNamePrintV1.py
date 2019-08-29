#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: yangyuyi
# @E-mail: TaroYoung2000@gmail.com
# @Date:   2019-08-29 07:48:16
# @Last Modified by:   yangyuyi
# @Last Modified time: 2019-08-29 08:27:19
#WeekNamePrintV1.py

weekStr="星期一星期二星期三星期四星期五星期六星期日"
weekId=input("请输入星期数字（1-7）：")
pos = (eval(weekId) - 1) * 3
print(weekStr[pos: pos+3])
