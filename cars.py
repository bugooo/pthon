#5 if语句
cars = ["audi","bmw","subaru","toyota"]
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#5.2 条件测试 and or == != >= > <= <
#5.2.6 检查特定值是否包含在列表中 in
requested_oppings = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_oppings)
print('pepperoni' in requested_oppings)
#5.2.7 检查特定值是否不包含在列表中
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(user.title()+",you can post a response if you wish")
#5.2.8 布尔表达式
game_active = True
can_edit = False

#5.3.2 if-else语句
age = 17
if age >= 18:
    print("you are old enough to vote.")
else:
    print("you are young")

#5.3.3 if-elif-else结构
age = 16
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your adminssion cost is $10.")
#5.3.4 使用多个elif代码块
age = 13
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age <= 65:
    price = 10
elif age > 65:
    price = 5
print("Your dmission cost is $"+str(price)+".")

#5.8 练习
username = ['admin','lilei','ana','tina']
if username:
    for name in username:
        print("Hello "+ name)
        if name == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello Eric, thankyou for logging in again")
else:
    print("We need to find some users!")
current_users = ['aaa','vvv','cccc','dddd','eeee']
new_users = ['aaa','vvv','rrr','www','mmmm']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user+" is existed")
    else:
        print(new_user+" is not existed")
num = list(range(1,10))
for n in num:
    if n == 1:
        print("1st")
    elif n == 2:
        print("2nd")
    elif n == 3:
        print("3rd")
    else:
        print(str(n)+"th")



    




