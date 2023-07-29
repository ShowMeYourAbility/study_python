"""
练习：在终端中输入商品单价、购买的数量和支付金额。计算应该找回多少钱。
效果：
请输入商品单价：5
请输入购买数量：3
请输入支付金额：20
应找回：5.0
"""
# 1.输入数据
unit_price = input("请输入商品单价：")
num = input("请输入购买数量：")
payment_amount = input("请输入支付金额：")

# 2.计算
unit_price = float(unit_price)
num = int(num)
payment_amount = float(payment_amount)
back_amount = payment_amount - unit_price * num

# 3.返回结果
print("应找回：" + str(back_amount))
