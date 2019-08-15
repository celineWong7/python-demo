# 1. list - 列表
# Python内置的一种数据类型。
# list是有序的集合，可以随时添加、删除其中元素
# eg1
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates) #['Michael', 'Bob', 'Tracy']
print(len(classmates)) #3

# 可以用索引方位list的每个位置的元素，索引从0开始
print(1, classmates[1]) # 1 Bob
print(0, classmates[0]) # 0 Michael
print(0, classmates[2]) # 2 Tracy
# print(3, classmates[3]) # 报错，因为索引超出范围。

print('len(classmates)-1', classmates[len(classmates)-1]) # 最后一个元素索引是len(classmates)-1

# 还可以用-1做索引，直接获取最后一个元素
# 以此类推，还可以用-2获取倒数第2个元素……
print(-1, classmates[-1]) # -1 Tracy
print(-2, classmates[-2]) # -2 Bob


# 2. list的增、删
# （1）append(item) 追加元素item到列表末尾
# （2）insert(index, item) 把元素item插入到指定索引index的位置
# （3）pop() 删除列表末尾的元素
# （4）pop(index) 删除指定索引位置的元素
# eg2
classmates.append('celine') # 在末尾追加元素
print(classmates) # ['Michael', 'Bob', 'Tracy', 'celine']

# classmates.append('celine2','celine3') # 会报错，因为每次只能追加一个元素
classmates.append('celine2')
print(classmates) # ['Michael', 'Bob', 'Tracy', 'celine', 'celine2']

classmates.insert(4,'celine1') # 在celine和celine2中间插入celine1
print(classmates) # ['Michael', 'Bob', 'Tracy', 'celine', 'celine1', 'celine2']

classmates.pop() # 删除最后一个元素
print(classmates) # ['Michael', 'Bob', 'Tracy', 'celine', 'celine1']

classmates.pop(0) # 删除第一个元素
print(classmates) # ['Bob', 'Tracy', 'celine', 'celine1']


# （5）替换元素：可以直接赋值
classmates[0] = 'Apple'


# （6）list里面的元素的数据类型也可以不同
classmates[1] = 100
classmates[3] = False
print(classmates) # ['Apple', 100, 'celine', False]


# （7）list元素也可以是另一个list
classmates[2] = ['A', 'A+', 'B']
print(classmates) # ['Apple', 100, ['A', 'A+', 'B'], False]
print(len(classmates)); # 4
