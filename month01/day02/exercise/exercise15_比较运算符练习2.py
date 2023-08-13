"""
练习2:输入一个数判断是不是正数
"""
a = int(input("请输入一个数:"))
if a > 0:
    print("是正数")
elif a < 0:
    print("是负数")
else:
    print("既不是正数，也不是负数")
