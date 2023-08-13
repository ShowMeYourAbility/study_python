"""
如果账号的密码错误3次，提示锁定账户，效果如下：
请输入账号：gtx
请输入密码：1234
登录失败
你还剩余 2次机会

请输入账号：Qtx
请输入密码：1234
登录失败
你还剩余 1次机会

请输入账号：Qtx
请输入密码：123456
登录成功
"""
times = 3
for i in range(times):
    account = input("请输入账号:")
    pwd = input("请输入密码：")
    if account == "Qtx" and pwd == "123456":
        print("登陆成功")
        break
    else:
        print("登陆失败")
        print("你还剩余" + str(times - i - 1) + "次机会")
