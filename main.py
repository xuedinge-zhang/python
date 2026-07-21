# print("Hello, World!")
# print("nihao")
# print("nihao")
# print("nihao")
# print("nihao")
# print("nihao")
# name = "传播博客"
# setup_year = 2006
# stock_price = 19.99
# message = ("%s成立于%d今天股价是%f")%(name,setup_year,stock_price)
# print(message)
# a = 111

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

# i= 1
# while i<=9:
#     j=1
#     while j<=i:
#         print(f"{j}*{i}={j*i}\t",end="")
#
#         j+=1
#     print()
#     i=i+1


# count = 0
# name = "itheima is a brand of itcastt"
# for x in name:
#     if x == "a":
#         count +=1
# print(f"一共有{count}个a")
#
# for x in range(10):
#     print(x)
#
# for x in range(5, 10):
#     print(x)
#
# for x in range(5, 10, 2):
#     print(x)

# i = 1
# for i in range(1, 101):
#     print(f"今天是向小美表白的第{i}天")
#
#     for j in range(1, 11):
#         print(f"给小美送的第{j}朵玫瑰花")
#
#     print("小美我喜欢你")


# for i in range(1,10):
#     for j in range(1,i+1):
#         print (f"{j} * {i} = {i*j}\t", end="")
#     print()

# yue = 10000
# for i in range(1,21):
#     import random
#     num = random.randint(1, 10)
#     if yue == 0:
#         print("工资发完了，下个月领取吧")
#         break
#     else:
#         if num >= 5:
#             yue -= 1000
#             print(f"向员工{i}发工资1000元，账户余额还剩{yue}元")
#         else:
#             print(f"员工{i}，绩效分{num}，低于5，不发工资，下一位")




# money = 5000000
# name = input("请输入您的姓名：")
# def cha(show_header):
#     if show_header:
#         print("----------查询余额----------")
#     print(f"{name}，您好，您余额剩余：{money}")
#
#
# def qu (num):
#     global money
#     if num > money:
#         print("余额不足")
#     else:
#         money-=num
#         print("----------取款----------")
#         print(f"{name}，您好，您取款{num}元成功")
#         cha(False)
#
# def cun(num):
#     print("----------存款----------")
#     global money
#
#     money +=num
#     print(f"{name}，您好，您取款{num}元成功")
#     cha(False)
#
# def main():
#     print("----------主菜单----------")
#     print(f"{name},您好，欢迎来到黑马银行ATM。请您选择操作：")
#     print("查询余额\t[输入1]")
#     print("存款\t\t[输入2]")
#     print("取款\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     return int(input("请输入您的选择"))
#
#
#
#
#
# while True:
#     kb = main()
#     if kb == 1:
#         cha(True)
#         continue
#
#
#     elif kb == 2:
#         num = int(input("请输入想要存多少钱："))
#         cun(num)
#         continue
#
#     elif kb == 3:
#         num = int(input("请输入想要取多少钱"))
#         qu(num)
#         continue
#
#     else:
#         break






# list = ["itt","ii","py"]
# a = list.pop(1)
# # 删除指定元素并返回出去
# print(f"{list},{a}")
#
#
#
# list = [1,1,1,1,1]
# print(len(list))


def list_while_func():


    list = [1, 2, 3, 4, 5, 6]


    index = 0
    while index < len(list):
        ele = list[index]
        print(f"{ele}")
        index += 1

list_while_func()