"""
加法计算器
效果：
请输入加数：3
请输入另一个加数：5
3+5=8
"""
# 1.输入数据
addend1 = int(input("请输入加数："))
addend2 = int(input("请输入另一个加数："))
# 2.运算
sum = addend1 + addend2
# 3.返回结果
print(str(addend1) + "+" + str(addend2) + "=" + str(sum))
