# input 让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便你使用
#message = input("Tell me something,and I will repeat it back to you: ")
#print(message)

#7.1.2 使用int()来获取数值输入
#age = input("how old are you?")
#age = int(age)
#print(age >= 18)

#7.1.3 求模运算符 % 将两个数相除并返回余数：
#number = input("Enter a number,and I will tell you if it's even or odd:")
#number = int(number)
#if number%2 == 0:
#    print("\n the number "+str(number)+" is even")
#else:
#    print("\n the number "+str(number)+" is odd")
#7.2.1 使用while循环
#current_number = 1
#while current_number <=5:
#    print(current_number)
#    current_number+=1
#7.2.2 让用户选择何时退出
#prompt = "\n Tell me something,and I will repeat it back to you:"
#prompt += "\n Enter 'quit' to end the program."
#message = ""
#while message != "quit":
#    message = input(prompt)
#    if message!="quit":
#        print(message)
#7.2.3 使用标志
#prompt = "\n Tell me something,and I will repeat it back to you:"
#prompt += "\n Enter 'quit' to end the program."
#active = True
#while active:
#    if message!="quit":
#        message = input(prompt)
#        print(message)
#    else:
#        active = False
#使用break退出循环

#prompt = "\n Please enter the name of a city you have visited:"
#prompt += "\n Enter 'quit' when you are finished."
#while True:
#    city = input(prompt)
#    if city =="quit":
#        break
#    else:
#      print("I'd love to go to "+city.title()+" !")

#7.2.5 在循环中使用continue
#current_number = 0
#while current_number < 10:
#    current_number+=1
#    if current_number % 2 == 0:
#        continue
#    print(current_number)

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user : "+current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
#删除包含特定值的所有列表元素
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#7.3.3 使用用户输入来填充字典
responses = {}
polling_active = True
while polling_active:
    name = input("\n What is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] =response
    repeat = input("Would you like to let an other persion respond?(yes/no)")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name,response in responses.items():
    print(name + " would like to climb "+response+".")