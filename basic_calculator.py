# define the function needed add , sub, mul, division
# print option to the user 
# ask for the values
# call the function
# while loop to continue the program untill the user want to exit

def add(a, b):
    ans = a + b 
    print (str(a) + " + " + str (b)+ " = " + str(ans) , "\n")

def sub(a, b):
    ans = a - b 
    print(str(a) + " - " +str(b)+ " = " +str(ans), "\n")

def mul(a, b):
    ans = a * b
    print ( str (a)+ " X " + str(b)+ " = " +str(ans), "\n")

def div(a, b):
    ans = a / b
    print(str (a)+ " / " + str(b)+ " = " +str(ans), "\n")


while True:
    print("A. Addition")
    print("S. Sunbstraction")
    print("M. Multipliction")
    print("D. Division")

    choice = input("input your choice ")

    if choice == "A" or choice == "a":
        print("Addition")
        a = int(input("Input First Number:- "))
        b = int(input("Input Second Number:-  "))
        add(a, b)

    elif choice == "S" or choice == "s":
        print("Substraction")
        a = int(input("Input First Number:- "))
        b = int(input("Input Second Number:-  "))
        sub(a, b)

    elif choice == "M" or choice == "m":
        print("Multiplication")
        a = int(input("Input First Number:- "))
        b = int(input("Input Second Number:- "))
        mul(a, b)

    elif choice == "D" or choice == "d":
        print("Division")
        a = int(input("Input First Number:- "))
        b = int(input("Input Second Number:-  "))
        div(a, b)

    elif choice == "E" or choice == "e":
        print("Programme Ended")
        quit()