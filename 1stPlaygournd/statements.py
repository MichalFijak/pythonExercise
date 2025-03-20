age = int(input("Enter age :"))

if(age>=18):
    print('true')
elif age<0:
    print('you are mistaken')
else:
    print('false')

#operators
x =True
if 20 >=0 and x:
    print("There's no && operators")



#shorthen

num=5

print("Positive" if num>0 else "Negative")

input("close terminal")