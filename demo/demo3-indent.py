
# eg1. 输出一个数的绝对值
a = 100
if a >= 0:
	print(a)
else:
	print(-a)

# 注意：
# 1. python语法采用缩进方式。一般约定4个空格的缩进。
# 2. 每一行都是一个语句，当语句以冒号结尾时，表示后面的缩进语句为代码块。（会在eg2详细说明）
# 3. 大小敏感

print('now is eg2.====================')

# eg2. 理解冒号和代码块
# python没有其他语言那样有{...} 或者 begin...end 来标识代码块，而是采用代码缩进和冒号来区分代码之间层次。

score = 90
if score > 80:
	print('excellent!')
	print('You are very good!')
elif score < 60:
	print('so sad.')
else:
	print('just so-so.')

# eg2中，大于80的判断，两个print缩进相同，则它们是一个代码块，满足条件时会一起执行。
# 注意：python里的else if和其他语言不同，直接就是一个简写单词elif。



# 具体可参考：[python的冒号和缩近](https://blog.csdn.net/u012803067/article/details/79124117)