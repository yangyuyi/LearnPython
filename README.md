# Python学习

## Keywords

> |       |        |          |       |        |          |
> | :---: | :----: | :------: | :---: | :----: | :------: |
> | False |  None  |   True   |  and  |   as   |  assert  |
> | break | class  | continue |  def  |  del   |   elif   |
> | else  | except | finally  |  for  |  from  |  global  |
> |  if   | import |    in    |  is   | lambda | nonlocal |
> |  not  |   or   |   pass   | raise | return |   try    |
> | while |  with  |  yield   |   -   |   -    |    -     |

1. False

```python
if q==False:#False
```

2. None
   表示该值是一个空对象，空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

```
>>>type(None)
<class 'NoneType'>
>>>type('')
<class ''str'>
```
*Ps:不太懂的亚子* 🧐

3. True

```python
if q==True:#True
```

4. and
   q and p: q和p都满足一定条件，**缺一不可**

```python
if (q and p):
	print("1 - 变量 q 和 p 都为 true")
```

5. as

```python
import turtle as t
```

6. assert
   assert断言语句：[【Python】【assert】assert断言语句](https://zhuanlan.zhihu.com/p/32017976)
   *Ps:暂时不太懂mark一下*

7. break
   break语句用在while和for循环中，用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。<br>如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。

```python
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      break
   print '当前字母 :', letter
  
var = 10                    # 第二个实例
while var > 0:              
   print '当前变量值 :', var
   var = var -1
   if var == 5:   # 当变量 var 等于 5 时退出循环
      break
 
print "Good bye!" 
```

**参考文献**：[Python break 语句 | 菜鸟教程](runoob.com/python/python-break-statement.html)

8. class
   用来创建类

```python
class Dog:
    def __init__(self,name):#类创建的时候便执行，常用来初始化类
    	self.name=name
    	self.__voice="wangwang"#__voice表示voice属性为私有属性
	def yell(self):#功能函数
		print self.__voice#yell函数用来打印私有变量__voice
```

9. continue

   重新执行循环<br>Python continue 语句跳出本次循环，而break跳出整个循环。<br>continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。<br>continue语句用在while和for循环中。

   **参考文献**：[Python continue 语句](https://www.runoob.com/python/python-continue-statement.html)

10. def & return
    创建函数
```python
def functionname( parameters ):#parameters是自定义参数
   "函数_文档字符串"
   function_suite
   return [expression]#expression是返回值，当调用functionname函数时，就会返回expression值
```
* **return**语句用于**退出函数**，向调用方返回一个表达式。
* **return在不带参数的情况下（或者没有写return语句），默认返回None。**
* python 函数返回值`return`，函数中**一定**要有return返回值才是完整的函数

11. del
	python中del删除的是变量，而不是数据
```
a=1       # 对象 1 被 变量a引用，对象1的引用计数器为1  
b=a       # 对象1 被变量b引用，对象1的引用计数器加1  
c=a       # 对象1 被变量c引用，对象1的引用计数器加1  
del a     #删除变量a，解除a对1的引用  
del b     #删除变量b，解除b对1的引用  
print(c)  #最终变量c仍然引用1  
```
关于list
```
li=[1,2,3,4,5]  #列表本身不包含数据1,2,3,4,5，而是包含变量：li[0] li[1] li[2] li[3] li[4]   
first=li[0]     #拷贝列表，也不会有数据对象的复制，而是创建新的变量引用  
del li[0]  
print(li)      #输出[2, 3, 4, 5]  
print(first)   #输出 1  
```
**参考文献**：[python 中del 的用法 - CSDN博客](https://blog.csdn.net/love1code/article/details/47276683)

12. if & elif & else
```python
if expression1:
    statement(s)
elif expression2:
    statement(s)
elif expression3:
    statement(s)
else:
    statement(s)
```

13. else & except & finally & try
这几个保留字放在一起说<br>常在python中用来**捕捉并处理异常**
```python
try:
    clause
except:
    clause#出现异常时执行
else:
    clause#不出现异常时执行
finally:
    clause#不管有无异常都要执行
```
<br>具体到错误<br>
```python
try:
    clause
except ValueError:
    clause#出现异常时执行
except ZeroDivisionError:
    clause#出现异常时执行
else:
    clause#不出现异常时执行
finally:
    clause#不管有无异常都要执行
```

14. for & in
```python
for i in range(100):
```

15. from & import
```python
from datetime import datetime#是只引入datetime包里的datetime类
import datetime#引入整个datetime包
```

16. global
申请全局变量<br><br>
在编写程序的时候，如果想为一个在函数外的变量重新赋值，并且这个变量会作用于许多函数中时，就需要告诉python这个变量的作用域是全局变量。此时用global语句就可以变成这个任务，也就是说没有用global语句的情况下，是不能修改全局变量的。
```
>>>x = 6
>>>def func():
>>>    global x
>>>    x = 1
>>>
>>>func()
>>>print x
1
```

17. 






