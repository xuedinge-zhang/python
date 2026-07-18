print("Hello, World!")
print("nihao")
print("nihao")
print("nihao")
print("nihao")
print("nihao")
name = "传播博客"
setup_year = 2006
stock_price = 19.99
message = ("%s成立于%d今天股价是%f")%(name,setup_year,stock_price)
print(message)
a = 111

# name = "风云公司"
# stock_price = 22.22
# stock_code = 100001
# stock_price_daily_growth_factor = 1.1
# growth_days = 12
# price = stock_price*stock_price_daily_growth_factor**growth_days
# print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_price}")
# print("每日增长系数是：%.2f,经过%d天的增长后,当前股价达到了：%.2f"%(stock_price_daily_growth_factor,growth_days,price))

# user_name = input("请输入用户名")
# user_type = input("请输入会员类型")
# print(f"您好；{user_name},您是尊贵的{user_type}用户，欢迎您的光临")

# import random
#
# num = random.randint(1,10)
# guess_num = int(input("输入你要猜测的数字："))
#
# if guess_num == num:
#     print("恭喜，第一次猜中了")
# else:
#     if guess_num > num:
#         print("你猜测的数字大了")
#     else:
#         print("你猜测的数字小了")
#
#     guss_num = int(input("再次输入你要猜测的数字："))
#     if guss_num == num:
#         print("恭喜，第二次猜中了")
#     else:
#         if guess_num > num:
#             print("你猜测的数字大了")
#         else:
#             print("你猜测的数字小了")
#         guess_num = int(input("再次输入你要猜测的数字"))
#
#         if guess_num == num:
#             print("恭喜，第三次猜中了")
#         else:
#             print("三次机会用完了，没有猜中。")

i= 1
while i<=9:
    j=1
    while j<=i:
        print(f"{j}*{i}={j*i}\t",end="")

        j+=1
    print()
    i=i+1