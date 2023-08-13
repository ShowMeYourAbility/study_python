"""
电梯设置规定：
如果承载人不超过10人，且总重量不超过1000千克，可以正常运行

步骤：
终端中获取人数/总重量
显示电梯正常运行还是电梯超载
"""
# 终端中获取人数/总重量
count_people = int(input("请输入人数："))
total_weight = float(input("请输入总重量(kg)："))
# 显示电梯正常运行还是电梯超载
if count_people <= 10 and total_weight <= 1000:
    print("正常运行")
else:
    print("电梯超载")
