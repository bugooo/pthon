class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+" is now sitting.")
    def roll_over(self):
        """模拟小狗呗命令时打滚"""
        print(self.name.title()+" rolled over!")

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type)
    def open_restaurant(self):
        print(" is Open")
my_restaurant = Restaurant("tiantianquan","test")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
restaurant1 = Restaurant("res1","type1")
restaurant2 = Restaurant("res2","type2")
restaurant3 = Restaurant("res3","type3")
restaurant1.describe_restaurant();
restaurant2.describe_restaurant();
restaurant3.describe_restaurant();
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
    def greet_user(self):
        print("Hello,"+self.last_name.title())
lilei = User("li","lei")
lilei.describe_user()
lilei.greet_user()

class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

    


