n=int(input("Enter the number of iterations: "))
a=0
b=1
print(a," ")
print(b," ")
i=1
while(i<=n):
 sum=a+b
 print(sum, " ")
 a=b
 b=sum
 i=i+1


