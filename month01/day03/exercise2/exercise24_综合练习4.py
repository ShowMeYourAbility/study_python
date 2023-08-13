"""
在终端中录入4个同学体重，打印最轻的值
效果：
请输入第1个同学体重：100
请输入第2个同学体重：120
请输入第3个同学体重：93
请输入第4个同学体重：160
最轻的同学：93
"""
least = 0
for i in range(4):
    weight = float(input("请输入第" + str(i + 1) + "个同学体重："))
    if i == 0:
        least = weight
    elif weight < least:
        least = weight
print("最轻的同学:" + str(least))
