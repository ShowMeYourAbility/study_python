"""
在终端中输入整数,打印正数、 负数、零
效果：
请输入一个整数：10
正数
"""
a=int(input("请输入一个整数："))
if a>0:
    print("正数")
elif a<0:
    print("负数")
else:
    print("零")