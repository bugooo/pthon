import csv
filename = 'pro_contents.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    print(head_row)