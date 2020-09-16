filename = 'programming.txt'
#以写入（'w'）模式打开文件时如果指定的文件已经存在，Python将在返回文件对象前清空该文件
with open(filename,'w') as file_object:
    file_object.write("I Love programming!\n")
    file_object.write("I love createing new games.\n")
#附加到文件
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets!\n")
    file_object.write("I also creating  apps that can run in a browser!\n")


