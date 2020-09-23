#异常
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divisor by zero!")
#使用异常避免崩溃
print("Give me two numbers,and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

#处理FileNotFoundError异常
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = 'Sorry,the file '+filename+" does not exist."
    print(msg)
