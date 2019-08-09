# 一、数据类型
# 1. 整数。可处理任意大小整数。十六进制和其他语言一样，以 0x为前缀。
# 2. 浮点数。也就是小数。科学计数法表示方式：314000 => 3.14e5, 0.0000012 => 1.2e-6。
# 3. 字符串。单引号或双引号括起来的任意文本。
# 4. 布尔值。True和False（注意：首字母必须大写）。
# 5. 空值。None（一个特殊的空值）
# 6. 列表、字典等

# eg1.
print('int:', -8080)
print('16base:', 0xf)
print('float:', 3.14e5)
print('string:','abc')
print('Boolean & None:',True,False,None)
print('3>2 is:', 3>2)
print('0<10 is:', 0<10)


# 二、转义字符 \
# \n 换行
# \t 制表符  
# \\ 表示一个\
# r'' 表示引号里面的内容默认不转义
# '''...''' 表示多行内容

print('\n\n==========eg2==========\n')
# eg2.
print('I\'m \"OK\"')
print(r'I\'m \"OK\"')
print('''line1
	... line2
	... line3''')


# 三、与、或、非运算
# python里的运算符是and or not

print('\n\n==========eg3==========\n')
# eg3.
print(True and True)
print(True and False)
print(True or False)
print(not True)
print(5>3 or 1>3)