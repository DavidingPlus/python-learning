"""
演示判断语句的嵌套使用
"""

# if int(input("您的身高是多少: ")) > 120:
#     print("身高超出限制,不可以免费")
#     print("但是,如果VIP等级大于3,可以免费")

#     if (int(input("您的VIP级别是多少: "))) > 3:
#         print("恭喜你,VIP级别达标,可以免费")
#     else:
#         print("Sorry,您需要买票,10元")
# else:
#     print("欢迎小朋友免费游玩")

age = 20
year = 3
level = 1
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的年龄达标了")
        if year > 2:
            print("恭喜你,年龄和入职时间都达标,可以领取礼物")
        elif level > 3:
            print("恭喜你,年龄和级别达标,可以领取礼物")
        else:
            print("不好意思,尽管年龄达标,但是入职时间和级别都不达标")

    else:
        print("不好意思,年龄太大了")
else:
    print("不好意思,小朋友不可以领取")
