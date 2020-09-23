#for 循环
magicians = ['alice','david','carolia']
for magician in magicians:
    print(magician)
#在for循环后面，没有缩进的代码都只执行一次，而不会重复执行
magicians = ['alice','david','carolina']
for magician in  magicians:
    print(magician.title()+",that was a great trick!")
    print("I can't wait to see your next trick,"+magician.title()+".\n")
print("Thank you,every.That was a great magic show!")
#根据缩进来判断代码行与前一个代码行的关系
#4.1练习
pizzas = ['aaaa','bbbb','ccccc']
for pizza in pizzas:
    print(pizza)
    print("I like "+pizza+" pizza")
print("I really love pizza!")
#4.2 练习
animals = ['cat','dog','bird']
for animal in animals:
    print(animal)
    print("A "+animal+" would make a great pet")
print("Any of these animals would make a great pet!")

#range()生成一系列数字 指定的第一个值开始数，并在到达你指定的第二个值后停止，因此输出不包含第二个值（这里为5）。
for value in range(1,5):
    print(value)
number = list(range(2,6))
print(number)
#使用函数range()时，还可指定步长。从2开始数，然后不断地加2，直到达到或超过终值（11）
even_numbers = list(range(2,11,2))
print(even_numbers)
# ** 表示乘方运算
squares = [];
for value in range(1,11):
    squares.append(value**2)
print(squares) 
squares = [value**2 for value in range(1,11)] 
print(squares) 
#min() max() sum()
digitis = [1,7,5,3,6,2,1,0,7,3]
print(min(digitis))
print(max(digitis))
print(sum(digitis))
#4-3练习
for value in range(1,21):
    print(value)
#4-5

number = list(range(1,1000001))
print(min(number))
print(max(number))
print(sum(number))
    
jishu = list(range(1,20,2))
print(jishu)
for value in jishu:
    print(value)
s = []
for value in range(1,11):
    s.append(value*3)
print(s)
a = []
for i in range(1,11):
    v = i**3
    a.append(v)
    print(v)
print(a)

squares = [value**3 for value in range(1,11)]
print(squares)

#切片
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
#如何没有指定第一个索引 将自动从列表开头开始
players = ['charles','martina','michael','florence','eli']
print(players[:4])

#省略终止索引可以提取到列表末尾的所有元素
players = ['charles','martina','michael','florence','eli']
print(players[2:])
#负数索引返回离列表末尾相应距离的元素
print(players[-3:])
#复制列表 
my_foods = ['pizza','falafel','carrot cake']
friend_food = my_foods[:]
print(my_foods)
print(friend_food)
my_foods.append("aaaa")
friend_food.append("bbb")
print(my_foods)
print(friend_food)

friend_food = my_foods
my_foods.append("ccc")
friend_food.append("ddd")
print(my_foods)
print(friend_food)

#Python将不能修改的值称为不可变的，而不可变的列表被称为元组
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#给元组变量赋值是合法的 但是不能修改元组的值
dimensions = (300,100)
for dimension in dimensions:
    print(dimension)
    
