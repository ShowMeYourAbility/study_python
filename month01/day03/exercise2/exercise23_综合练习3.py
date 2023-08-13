"""
如果是vip客户，消费小于等于500，享受85折
消费大于500，享受8折
如果不是vip客户，消费大于等于800，享受9折
消费小于800，原价
在终端中输入账户类型，消费金额，计算折扣。
"""
# 在终端中输入账户类型，消费金额
is_vip = input("请输入是不是vip客户（y表示是；非y表示不是）：") == "y"
consume_amount = float(input("请输入消费金额："))
# 计算折扣
if is_vip:
    if consume_amount > 500:
        print("8折")
    else:
        print("85折")
else:
    if consume_amount > 800:
        print("9折")
    else:
        print("原价")
