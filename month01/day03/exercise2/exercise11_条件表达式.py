"""
第10行等效于第4行到第7行，一行顶四行
"""
if input("请输入您的性别：") == "男":
    value = 1
else:
    value = 0
print("根据您输入的性别，value的值为：" + str(value))

value = 1 if input("请输入您的性别：") == "男" else 0
print("根据您输入的性别，value的值为：" + str(value))
