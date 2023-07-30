# 1、输入数据
h1 = float(input("请输入第一个人的身高："))
h2 = float(input("请输入第二个人的身高："))
h3 = float(input("请输入第三个人的身高："))
h4 = float(input("请输入第四个人的身高："))
# 2、找出最大值
h = 0
if h1 > h:
    h = h1
if h2 > h:
    h = h2
if h3 > h:
    h = h3
if h4 > h:
    h = h4
# 3、返回结果
print(h)
