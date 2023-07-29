"""
汇率转换器
假设汇率为6.405
效果：
请输入美元：18.4
18.4美元=117.85人民币
"""
# 1.输入数据
us_dollar = float(input("请输入美元"))
# 2.运算
rmb = us_dollar * 6.405
rmb = round(rmb, 2)
# 3.返回结果
print(str(us_dollar) + "美元=" + str(rmb) + "人民币")
