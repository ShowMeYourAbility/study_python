"""
在终端输入年份和月份，打印当月的天数
规则：
    1、3、5、7、8、10、12月有31天
    4、6、9、11月有30天
    闰年2月有29天，平年有28天
效果：
    请输入月份：10
    31天
"""
month = int(input("请输入月份："))
year = int(input("请输入年份"))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31" + "天")
if month == 4 or month == 6 or month == 9 or month == 11:
    print("30" + "天")
if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("29" + "天")
    else:
        print("28" + "天")
