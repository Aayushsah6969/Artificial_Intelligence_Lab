# a=int(input("Enter first number: "))
a=input("Enter first number: ")
b=int(input("Enter second number: "))
if(isinstance(a,int)):
    print("First input is an integer")
else:
    a=int(a)
    print("First input converted to integer")
if(isinstance(b,int)):
    print("Second input is an integer")
else:
    b=int(b)
    print("Second input converted to integer")
sum=a+b
print("The sum of",a,"and",b,"is",sum)
# print(f"sum = {sum}")