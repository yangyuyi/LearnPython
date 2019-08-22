#Python学习
-----
##Keywords
> |       |        |          |       |        |          |
> | :---: | :----: | :------: | :---: | :----: | :------: |
> | False |  None  |   True   |  and  |   as   |  assert  |
> | break | class  | continue |  def  |  del   |   elif   |
> | else  | except | finally  |  for  |  from  |  global  |
> |  if   | import |    in    |  is   | lambda | nonlocal |
> |  not  |   or   |   pass   | raise | return |   try    |
> | while |  with  |  yield   |   -   |   -    |    -     |

1.False
```python
if q==False:#False
```
2.None(?)

3.True
```python
if q==True:#True
```

4.and
q and p: q和p都满足一定条件，**缺一不可**
```python
if (q and p):
	print("1 - 变量 q 和 p 都为 true")
```

5.as
```python
import turtle as t
```

6.assert
assert断言语句：[【Python】【assert】assert断言语句](https://zhuanlan.zhihu.com/p/32017976)
*Ps:暂时不太懂mark一下*

7.break
break语句用在while和for循环中，用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。

如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。

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

8.class


