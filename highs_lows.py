import csv
filename = 'pro_contents.csv'
with open(filename) as f:
    '''创建一个与该文件相关联的阅读器（reader）对象'''
    reader = csv.reader(f)
    '''函数next()'''
    head_row = next(reader)
    print(head_row)