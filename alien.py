# 在Python中，字典用放在花括号{}中的一系列健-值对表示
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
#6.2.2 添加键—值对
alien_0 = {'color':'green','points':5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y——position'] = 25
print(alien_0)
#6.2.3 先创建一个空字典  可先使用一对空的花括号定义一个字典，再分行添加各个键—值对
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
#6.2.5 删除键—值对 对于字典中不再需要的信息，可使用del语句将相应的键—值对彻底删除
alien_0 = {'color':'green','points':5}
del alien_0['points']
print(alien_0)
favorite_lanuages ={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print(favorite_lanuages)
print("Sarah's favorite language is "+
    favorite_lanuages['sarah'].title()+
    ".")

people = {"first_name":"huhu","last_name":"hehe","age":"26","city":"huoxing"}
print(people['first_name'])
print(people['last_name'])
print(people['age'])
print(people['city'])

#遍历所有键值对
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
for key,value in user_0.items():
    print("\nKey: "+key)
    print("Value: "+value)


#6.3.2 遍历字典中的所有键 keys()
for name in user_0.keys():
    print(name.title())
for name in user_0:
    print(name.title())


favorite_lanuages ={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
if "erin" not in favorite_lanuages.keys():
    print("Erin,please take our poll!")

#使用函数sorted()来获得按特定顺序排列的键列表的副本
favorite_lanuages ={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name in sorted(favorite_lanuages.keys()):
    print(name.title()+" thank you for take our poll!")

#6.3.4遍历字典中的所有值 values()
favorite_lanuages ={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print("The following languages have been mentioned")
for language in favorite_lanuages.values():
    print(language.title())
#为剔除重复项，可使用集合（set)
favorite_lanuages ={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print("The following languages have been mentioned")
for language in set(favorite_lanuages.values()):
    print(language.title())

#6.4 嵌套
alien_0 = {'color':'green','points':'5'}
alien_1 = {'color':'yellow','points':'10'}
alien_2 = {'color':'red','points':'15'}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
#6.4.2 在字典中存储列表
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
print("You ordered a "+pizza['crust']+"-crust pizza "+"With the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)

#6.4.3 在字典中存储字典
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'priceton',
    },
    'mcurie':{
        'first':'maria',
        'last':'curia',
        'location':'paris',
    },
}
for username,userinfo in users.items():
    print("\n Username: "+username)
    full_name = userinfo['first']+" "+userinfo['last']
    location = userinfo['location']
    print("\r Full name: " +full_name.title())
    print("\r location: "+location.title())

