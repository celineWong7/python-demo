# 1. tuple 元组
# 另一种有序列表，和list非常相似，但tuple一旦初始化就不能修改。
# 所以tuple没有append() insert() pop()这些方法，也不能赋值成其他元素。
# tuple获取元素和list一样，也是通过索引获取。
# eg1
# list定义时使用中括号，tuple定义时使用小括号
# eg1
fruit = ('apple', 'orange', 'banana')
print(fruit)

# fruit.append('hehe') # 报错
# fruit[1] = 'haha' # 报错


# 不可变的tuple有什么意义？
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。


# 2.tuple陷阱
# （1）定义一个只有1个元素的tuple时，必须加一个逗号，来消除歧义
# eg2

# 定义一个空tuple
t = () # ()

# 定义一个只有1个元素的tuple时
t1 = (1) # 1，这个是数字1
t2 = (1,) # (1,) 
print(t)
print(t1)
print(t2)

# 因为括号()既可以表示tuple，又可以表示数学公式中的小括号。
# Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
# 所以，Python在显示只有1个元素的tuple时，也会加一个逗号,，以免误解成数学计算意义上的括号。


#（2）“可变的”tuple
# eg3
tt = ('a', 'b', ['x', 'y'])
tt[2][0] = 'm'
tt[2][1] = 'n'
print(t) #('a', 'b', ['m', 'n'])

# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list。
# 所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
# 理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。