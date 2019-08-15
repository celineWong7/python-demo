# 循环
# 循环语句常见就是for和while，在Python对应就是for...in... 和 while
# 同样有break和continue关键字来提前结束循环
# 1. for in
# eg1 遍历输出
names = ['Bob', 'Celine', 'Yami']
for name in names:
	print(name)


# eg2 求和
s = 0
for x in [1,2,3,4,5]:
	s = s+x
print(s)


# eg3 range(start, stop[, step]) 生成整数序列
# start - 计算从start开始。默认是0。range(5) 等价于 range(0, 5)
# stop - 计数从stop结束，但不包含stop。range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step - 步长，默认1.

print(range(6)) # [0,1,2,3,4,5]
