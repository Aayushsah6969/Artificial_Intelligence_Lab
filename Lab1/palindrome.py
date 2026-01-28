a=input("Enter a string or number:  ")
b=a[::-1]
print(b)  #a[start:stop:step]
if(a==b):
    print(f"{a} is a palindrome")
else: 
    print(f"{a} is not a palindrome")