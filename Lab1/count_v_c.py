str=input("Enter a string: ")
# print(type(str))
v=0
c=0
for s in str:
 if(s=='a' or s=='e' or s=='i' or s=='o' or s=='u'):
#   print(f"{s} is a vowel")
  v=v+1
 else:
    # print(f"{s} is a consonant")
    c=c+1
print(f"{v} vowels and {c} consonants found in the string.")

print("Approach 2: ")
v=0
c=0
for s in str:
  if(s.lower() in 'aeiouAEIOU'):
    v=v+1
  else:
    c=c+1
print(f"{v} vowels and {c} consonants found in the string.")
  