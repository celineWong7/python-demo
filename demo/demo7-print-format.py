# 输出格式化字符
# 1. 在Python中，采用的格式化方式和C语言是一致的，用%实现。
# %d: 整数
# %f: 浮点数
# %s: 字符串
# %x: 十六进制整数
# 
# %? 其实可以看做是一个占位符，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。
# eg1
print('Hello, %s. Nice to meet you.' % 'Celine') # 只有一个占位符时，后面提供值（变量）时，可以省略小括号
print('Hi, %s. You have %d apples.' % ('Mike', 10))



# 2. 格式化整数和浮点数，可以在格式化中指定是否补0，还可以指定位数。
# eg2
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# 3. 不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
# 4. 若希望字符串里面的%能作为普通字符输出，则需要转义： 用%%表示%
# eg3
print('Name: %s, Age: %s, isGirl: %s' %('Celine', 23, True))
print('The grouwth rate: %d%%' % 6)



# 5. format()方法
# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……
# eg5
print('Hello, {0}. Your score is {1: .1f}. '.format('xiaoming', 17.25))