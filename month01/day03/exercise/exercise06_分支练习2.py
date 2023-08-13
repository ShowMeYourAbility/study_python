"""
在终端中输入整数,打印正数、 负数、零
效果：
请输入一个整数：10
正数
"""
number = int(input("请输入一个整数："))
if number > 0:
    print("正数")
if number < 0:
    print("负数")
if number == 0:
    print("零")
