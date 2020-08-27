#列表
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[-1])#返回列表最后一个元素 列表为空时访问最后一个元素会报错
#3.1
names = ['lilei','laowang','lulu','lily']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print("his name is "+names[3]+".")
names[0] = "duchati"
print(names)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0,'test')
print(motorcycles)
del motorcycles[1]
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
first_owned = motorcycles.pop(1)
print(motorcycles)
print(first_owned)
motorcycles.remove('test')
print(motorcycles)
#sort()永久排序 按字母顺序 sort(reverse = True) 按字母相反的顺序
cars = ['bmw','audi','toyota','subaru']
cars.sort();
print(cars);
cars.sort(reverse=True)
print(cars)

#sorted临时排序
cars = ['bmw','audi','toyota','subaru']
print(sorted(cars))
print(cars)
#要反转列表元素的排列顺序，可使用方法reverse()
cars.reverse();
print(cars)
#len() 使用函数len()可快速获悉列表的长度
print(len(cars))