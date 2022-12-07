import function

a = function.add
s = function.subtract
m = function.multiply
d = function.divide

print("<<< Select operation. >>>")
print("    1.Add")
print("    2.Subtract")
print("    3.Multiply")
print("    4.Divide\n")


while True:
    
    choice = input("Enter choice: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", a(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", s(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", m(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", d(num1, num2))
        
        more = input("Solve one more? (<<< yes/no >>>): ")
        if more == "no":
            print("Okay, have a nice day!")
        break
    
    else:
        print("Invalid Input")