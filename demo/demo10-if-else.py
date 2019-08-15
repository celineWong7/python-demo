# 条件判断 if-elif-else
# python的条件语句关键字和其他语言类似，只有else if被整合elif了。
# 另外要注意的就是代码结构。因为python没有{}，所以它的语句块是靠冒号和缩进。
# eg1
age = 20
if age >= 6:
	print('teenager')
elif age >= 18:
	print('adult')
else:
	print('kid')


#eg2 
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False

# x = 0
# x = ''
# x = []
x = ()
if x:
	print('True')
else:
	print('False')


# eg3
# 注意input()的数据类想是str，若要和整数比较，就用int()转换数据类型
s = input('birth year:')
birth = int(s)
if birth < 2000:
	print('00前')
else:
	print('00后')