
# 一、编码
# 编码的由来和历史可以直接网上搜，此处简略做个说明：
# ASCII码：最早的127个字符，主要是大小英文字母、数字和一些符号。—— 采用1个字节
# GB2312：中文编码。
# ……后来各国语言都有自己的编码，在多语言混合文本开始出现了乱码……
# Unicode标准：把所有语言统一到一套编码里。—— 采用2个字节
# UTF-8编码：可变长编码。把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。


# 二、字符串
# 1. Python3中，字符串是以Unicode编码的
# 2. 对于单字符编码：
#    ord()：获取字符的整数，
#    chr()：获取编码对应的字符。
# eg1
# 注意：在git bash命令窗口是不识别中文的，所以window系统下，可以在DOS命令窗口
print('中文和English混合')
print('A', ord('A'))
print('王', ord('王'))
print(66, chr(66))
print(20013, chr(20013))


print('\n\n================eg3==============')
# 3. 对于普通字符串'abc'，因为是以Unicode表示，所以一个字符赌赢若干字节
# 若要把字符串变成以字节为单位的字节类型（bytes），可以用b作前缀
# eg3
import sys
x = b'abc'
y = b"ABC"
x_ = 'abc'
print(x, len(x), sys.getsizeof(x)) # b'abc' 3 36
print(x_, len(x_), sys.getsizeof(x_)) # abc 3 52



print('\n\n================eg4==============')
# 4. 编码与解码
# encode(): 如果要在网络上传输，或者保存到磁盘上，需要把str变为以字节为单位的bytes，可以用encode()。
# decode(): 若是从网络或磁盘上读取了字节流，那么读到的数据就是bytes，可以用decode()把bytes转换成str。
# eg4
print('ABC', 'ABC'.encode('ascii')) # b'ABC'
print('中文', '中文'.encode('utf-8')) # b'\xe4\xb8\xad\xe6\x96\x87'
# print('中文', '中文'.encode('ascii')) # 会报错，因为中文编码超过ASCII编码范围.（报错了会中断程序，若想继续执行代码，注释掉该句）

print(b'ABC', b'ABC'.decode('ascii')) #ABC
print(b'\xe4\xb8\xad\xe6\x96\x87', b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')) # 中文

# print(b'\xe4\xb8\xad\xef', b'\xe4\xb8\xad\xff'.decode('utf-8')) #包含无法解码字节时，会报错（报错了会中断程序，若想继续执行代码，注释掉该句）
print(b'\xe4\xb8\xad\xef', b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')) # 中 #若只有一小部分无效字节，可以通过errors='ignore'忽略错误字节




print('\n\n================eg5==============')
# 5. 字符串长度 len()
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
# eg5
print(len('ABC')) # 3
print(len('中文')) # 2

print(len(b'ABC')) # 3
print(len(b'\xe4\xb8\xad\xe6\x96\x87')) # 6
print(len('中文'.encode('utf-8'))) # 6


# 6. Python源码文件指定UTF-8编码
# （1）当源码包含中文时，为了让Python解释器读取源代码时，为了让它按UTF-8编码读取，通常在文件开头写上两行说明语句（注释语句）：
# #!/usr/bin/env python3     表示：为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# #-*- coding: utf-8 -*-     表示：为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# （2）在报错.py文件时，也要确保文本编辑器是使用UTF-8 without BOM编码





