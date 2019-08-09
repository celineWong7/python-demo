# 输入内容会存在变量name中
name = input()
print('Hello,',name)


# 输入提示文字
name = input('Please enter your name:')
print('Hi~,',name)

# 计算题
# 注意：输入的内容都是字符串，需要转成数值才能进行计算
a_ = input('Please input long: ')
b_ = input('Please input width: ')
a = float(a_)
b = float(b_)
print('Circumference: ', (a+b)*2)
print('Square: ', a*b)
