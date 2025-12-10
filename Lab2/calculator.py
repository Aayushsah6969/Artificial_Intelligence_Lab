print("WELCOME TO THE ADVANCED CALCULATOR \n")
print("Select operation to do: \n" \
"1. Add \n"\
"2. Subtract \n"\
"3. Multiply \n"\
"4. Divide \n"\
"00. Exit \n")


def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

while True:
 choice = int(input("Enter your choice: "))
 
 if choice == 1:
     num1 = int(input("Enter first number: "))
     num2 = int(input("Enter second number: "))
     print("Sum = ",add(num1, num2))
 elif choice == 2:
     num1 = int(input("Enter first number: "))
     num2 = int(input("Enter second number: "))
     print("Difference = ",subtract(num1, num2))
 elif choice == 3:
     num1 = int(input("Enter first number: "))
     num2 = int(input("Enter second number: "))
     print("Product = ",multiply(num1, num2))
 elif choice == 4:
     num1 = int(input("Enter first number: "))
     num2 = int(input("Enter second number: "))
     print("Quotient = ",divide(num1, num2))
 elif choice == 00:
     print("Exiting the Calculator. Goodbye!")
     break
     
 else:
     print("Enter a valid Choice!! ")