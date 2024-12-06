num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))

def sol(a, b, c):
    add_ = num1 + num2 + num3
    print("The sum of {}, {} and {} is: {}".format(num1, num2, num3, add_))

sol(num1, num2, num3)
