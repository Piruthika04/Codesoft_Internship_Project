
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


def calculator():
    print("Simple Calculator")


    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    
    if choice == '1':
        print(f"The result is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == '4':
        if num2 != 0:
            print(f"The result is: {divide(num1, num2)}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid input")

if __name__ == "__main__":
   calculator()



