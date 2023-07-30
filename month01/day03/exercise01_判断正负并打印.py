"""
输入一个整数
如果是正数显示正数，
如果是负数显示负数负数
如果是0显示0

效果：
请输入一个整数：10
正数
"""
num = int(input("请输入一个整数:"))
if num > 0:
    print("正数")
elif num < 0:
    print("负数")
else:
    print("0")