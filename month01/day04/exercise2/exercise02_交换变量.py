"""
哥哥的食物（food_of_elder_brother）是披萨（pizza）
弟弟的食物（food_of_younger_brother）的食物是牛排（beefsteak）
用两种方法交换两人的食物
（提示：如果不会的话，将上面的题目复制给poe，但要告诉poe用python实现）
"""
# ================== 方法一 =========================
food_of_elder_brother = "pizza"
food_of_younger_brother = "beefsteak"
print("哥哥的食物是：" + food_of_elder_brother)
print("弟弟的食物是：" + food_of_younger_brother)
# 先把哥哥的披萨放空碗里
bowl = food_of_elder_brother
# 再把弟弟的牛排放到哥哥碗里
food_of_elder_brother = food_of_younger_brother
# 再把碗里的披萨放弟弟的碗里
food_of_younger_brother = bowl
print("哥哥的食物是：" + food_of_elder_brother)
print("弟弟的食物是：" + food_of_younger_brother)

# ================== 方法二 =========================
food_of_elder_brother, food_of_younger_brother = food_of_younger_brother, food_of_elder_brother
print("哥哥的食物是：" + food_of_elder_brother)
print("弟弟的食物是：" + food_of_younger_brother)
