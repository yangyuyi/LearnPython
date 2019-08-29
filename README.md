# Python学习

## Keywords

<br>参考文献：[保留字详解](https://zhuanlan.zhihu.com/p/31967407)

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
if q==False:   #False
```

2. None
   <br>表示该值是一个空对象，空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

```
>>>type(None)
<class 'NoneType'>
>>>type('')
<class ''str'>
```

*Ps:不太懂的亚子* 🧐

3. True

```python
if q==True:   #True
```

4. and
   <br>q and p: q和p都满足一定条件，**缺一不可**

```python
if (q and p):
  print("1 - 变量 q 和 p 都为 true")
```

5. as

```python
import turtle as t
```

6. assert
   <br>assert断言语句：[【Python】【assert】assert断言语句](https://zhuanlan.zhihu.com/p/32017976)
   <br>*Ps:暂时不太懂mark一下*
7. break
   <br>break语句用在while和for循环中，用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。<br>如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。

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
   <br>用来创建类

```python
class Dog:
    def __init__(self,name):    #类创建的时候便执行，常用来初始化类
      self.name=name
      self.__voice="wangwang"    #__voice表示voice属性为私有属性
  def yell(self):#功能函数
    print self.__voice    #yell函数用来打印私有变量__voice
```

9. continue
   <br>重新执行循环<br>Python continue 语句跳出本次循环，而break跳出整个循环。<br>continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。<br>continue语句用在while和for循环中。

   **参考文献**：[Python continue 语句](https://www.runoob.com/python/python-continue-statement.html)

10. def & return
    <br>创建函数

```python
def functionname( parameters ):   #parameters是自定义参数
   "函数_文档字符串"
   function_suite
   return [expression]    #expression是返回值，当调用functionname函数时，就会返回expression值
```

- **return**语句用于**退出函数**，向调用方返回一个表达式。
- **return在不带参数的情况下（或者没有写return语句），默认返回None。**
- python 函数返回值`return`，函数中**一定**要有return返回值才是完整的函数

11. del
    <br>python中del删除的是变量，而不是数据

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
    <br>这几个保留字放在一起说<br>常在python中用来**捕捉并处理异常**

```python
try:
    clause
except:
    clause  #出现异常时执行
else:
    clause  #不出现异常时执行
finally:
    clause  #不管有无异常都要执行
```

具体到错误

```python
try:
    clause
except ValueError:
    clause  #出现异常时执行
except ZeroDivisionError:
    clause  #出现异常时执行
else:
    clause  #不出现异常时执行
finally:
    clause  #不管有无异常都要执行
```

14. for & in

```python
for i in range(100):
```

15. from & import

```python
from datetime import datetime   #是只引入datetime包里的datetime类
import datetime   #引入整个datetime包
```

16. global
    <br>**申请全局变量**<br><br>
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

17. is
    <br>
    is 主要是判断 2 个变量是否引用的是同一个对象，如果是的话，则返回 `True`，否则返回`false`<br>
    **即两个对象的id要相同，引用同一块区域。**
    <br>
    <br>**注意**⚠️：判断数字相等不要用 is 操作符

```
>>> a = 256
>>> b = 256
>>> id(a)
9987148
>>> id(b)
9987148
>>> a = 257
>>> b = 257
>>> id(a)
11662816
>>> id(b)
11662828
```

**is 相等代表两个对象的 id 相同(从底层来看的话，可以看作引用同一块内存区域)。**<br>所以即使数值相同，a与b依旧不同。

18. lambda
    <br>lambda作为一个表达式，定义了一个匿名函数，上例的代码x为入口参数，x+1为函数体

```
>>> g=lambda x:x+1
>>> g(1)
2
>>> g(2)
3
```

19. nonlocal
    <br>
    **非局部变量**<br>
    *Ps:这是python3新增的关键词*<br>
    **参考文献**：[【Python】【nonlocal】【global 】nonlocal非局部变量、global 全局变量、局部变量](https://zhuanlan.zhihu.com/p/32050475)
20. not

```python
if not( q and p ):
   print "变量 q 和 p 都为 false，或其中一个变量为 false"
```

21. or

```python
if ( a or b ):
   print "变量 a 和 b 都为 true，或其中一个变量为 true"
```

22. pass
    <br>Python pass是空语句，是为了保持程序结构的完整性。
    <br>pass 不做任何事情，一般用做占位语句。

```python
for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块'
   print '当前字母 :', letter

print "Good bye!"
```

**参考文献**：[Python pass 语句 | 菜鸟教程](https://www.runoob.com/python/python-pass-statement.html)

23. raise
    **触发异常**<br>
    当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。一旦执行了raise语句，raise后面的语句将不能执行

```python
try:
     s = None
     if s is None:
         print "s 是空对象"
         raise NameError     #如果引发NameError异常，后面的代码将不能执行
     print len(s)  #这句不会执行，但是后面的except还是会走到
except TypeError:
     print "空对象没有长度"



s = None
if s is None:
    raise NameError 
print 'is here?' #如果不使用try......except这种形式，那么直接抛出异常，不会执行到这里
```

**参考文献**：[python中异常处理--raise的使用 - 远游骑士 - 博客园](https://www.cnblogs.com/zhangyin6985/p/7229553.html)

24. while
    <br>Python 编程中 `while` 语句用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务。其基本形式为：

```python
while 判断条件：
  执行语句……
```

执行语句可以是单个语句或语句块。判断条件可以是任何表达式，任何非零、或非空（null）的值均为true<br>
当判断条件假false时，循环结束。

```python
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
 
print "Good bye!"
```

25. with & yield
    <br>
    with语句：[【Python】【with】with语句](https://zhuanlan.zhihu.com/p/32122124)<br>
    yield语句：[【Python】【yield】yield详解](https://zhuanlan.zhihu.com/p/32178981)<br>
    *Ps:一点高级可能暂时用不上吧emm*

## turtle库

### 画笔控制函数

**画笔操作后一直有效，一般成对出现**<br>

- turtle.penup() or turtle.pu()<br>
  func:拾起画笔
- turtle。pendown() or turtle.pd()<br>
  func:落下画笔
- turle.pensize(width) or turtle.width(width)<br>
  func:设置画笔宽度
- turtle.pencolor(color) color为颜色字符串或RGB值<br>
  func:设置画笔颜色<br>
  Ps:color的参数有3种形式:
  - 颜色字符串：turtke.pencolor("purple")
  - RGB的小数值：turtle.pencolor(0.63,0.13,0.94)
  - RGB的元组值：turtle.pencolor((0.63,0.13,0.94))

### 运动控制函数

**控制海龟行进：走直线 & 走曲线**

- turtle.forward(d) or turtle.fd(d)<br>
  func:向前行进 -d:行进距离，可以为负数,单位：像素（pixel）
- turtle.circle(r,extent=None)<br>
  func:根据半径r绘制extent角度的弧形 -r:默认圆心在海关左侧距离r距离的位置 -extent:绘制角度，默认是360度整圆

### 方向控制函数

**控制海龟面对方向绝对角度 & 海龟角度**

- turtle.setheading(angle) ot turtle.seth(angle)<br>
  func:改变行进方向 -angle:改变的某一个绝对角度
- turtle.left(angle)<br>
  func:turtle向左转angle度
- turtle.right(angle)<br>
  func:turtle向右转angle度

## 循环语句

**按照一定次数循环执行一组语句**

```python
for <variable> in range(<parameters>):
  <executed statement>
```

## range() 函数

**产生循环计数序列**

- range(N)
  func:产生0到N-1的整数序列，共N个
- range(M,N)
  func:产生M到N-1的整数序列，共N-M个

## 字符串

### 字符串切片高级用法
**使用[M：N：K]根据步长对字符串切片**<br>
- <字符串>[M:N],M缺失表示*至开头*,N缺失表示*至结尾*
- <字符串>[M:N:K],根据步长K对字符串切片<br>
常用方法：字符串逆序：s=s[::-1]

### 字符串的特殊字符
#### 转义符\
- 转义符表达特定字符的本意<br>
eg."\b" 回退<br>
   "\n" 换行<br>
   "\r" 回车（光标移动到本行首）

### 字符串操作符
**由0个或多个字符组成的有序字符序列**
|操作符及使用|               描述               |
| :------: | :-----------------------------: |
|   x+y    |         连接两个字符串x和y         |
|n*x or x*n|           复制n次字符串x           |
|  x in s  |如果x是s的字串，返回True，否则返回False|

### 字符串处理方法
**“方法”在编程中是一个专有名词**
- “方法”特指<a>.<b>()风格中的函数<b>()<br>
- “方法”本身也是函数，但与<a>有关<br>
- 字符串及变量也是<a>，存在一些方法<br>
<br>
**一些以方法形式提供的字符串处理功能**
|方法及使用|描述|
|:---:|:---:|
|str.lower() or str.upper()|返回字符串的副本，全部字符小写/大写|
|str.split(sep=None)|返回一个列表，由str根据sep被分割的部分组成|
|str.count(sub)|返回子串sub在str中出现的次数|
|str.replace(old,new)|返回字符串副本，所有old子串被替换为new|
|str.centre(width[,fillchar])|字符串str根据宽度width居中，fillchar可选|
|str.strip(chars)|从str中去掉在其左侧和右侧chars中列出的字符|
|str.join(iter)|在iter变量除最后元素外每个元素后增加一个str|

###字符串类型的格式化
**格式化是对字符串进行格式表达的方式**
- 字符串格式化使用.format()方法，用法如下：<br>
<teleplate string>.format(<逗号分隔的参数>)

#### 槽内部对格式化的配置方式
{<参数序号>：<格式控制标记>}<br>
|:|<填充>|<对齐>|<宽度>|<,>|<.精度>|<类型>|
|:--:|:--:|:--:|:--:|:--:|:--:|
|引导符号|用于填充的字符|< 左对齐<br> > 右对齐<br> ^ 居中对齐|槽设定的输出宽度|数字的千位分隔符|浮点数小数精度或字符串最大输出长度|整数类型<br>b,c,d,o,x,X<br>浮点数类型<br>e,E,f,%|

## time库
**time库是Python中处理时间的标准库**
- 计算机时间表达
- 提供获取系统时间并格式化输出功能
- 提供系统级精确计时功能，用于程序性能分析
```python
import time
time.<b>
```















































