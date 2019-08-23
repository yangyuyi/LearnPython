#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: yangyuyi
# @E-mail: TaroYoung2000@gmail.com
# @Date:   2019-08-19 20:47:45
# @Last Modified by:   yangyuyi
# @Last Modified time: 2019-08-22 21:12:27
#PythonDraw.py

import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
