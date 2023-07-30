"""
在终端输入年份和月份，打印当月的天数
规则：
    1、3、5、7、8、10、12月有31天
    4、6、9、11月有30天
    闰年2月有29天，平年有28天
    其他月份：月份不合法
效果：
    请输入年份：2023
    请输入月份：10
    2023年10月：31天
"""
year = int(input("请输入年份："))
month = int(input("请输入月份："))
# 是不是闰年
if year % 4 == 0 and year % 4 > 0 or year % 400 == 0:
    is_leap_year = True
else:
    is_leap_year = False
# 判断
if 1 <= month <= 12:
    if month == 4 or month == 6 or month == 9 or month == 11:
        print(str(year) + "年" + str(month) + "月：31天")
    elif month == 2 and is_leap_year:
        print(str(year) + "年" + str(month) + "月：29天")
    elif month == 2 and not is_leap_year:
        print(str(year) + "年" + str(month) + "月：28天")
    else:
        print(str(year) + "年" + str(month) + "月：30天")
else:
    print("月份不合法")
