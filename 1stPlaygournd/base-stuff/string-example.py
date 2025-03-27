

#result = len(name)
#result = name.find(" ")
#result = name.rfind("3")
#result = name.isdigit()
# result = name.isalpha()
# print(result)
# print(help(str))

# name = input("Enter some string:")

# def validate(name:str):
#     if len(name)>12:
#         print("Username is too long!")
#     elif  name.find(" ") !=-1:
#         print("Username contain spaces")
#     elif name.isdigit():
#         print("Username contain digits")

# validate(name)

#indexing
# name = "123-45-65"
# print(name[0:2])
# print(name[-2])
# print(name[::3])

# revert = name[::-1]
# print(revert)

price1 =3.1243
price2=-987.45
price3=12.34

print(f"Price 1 is {price1:+^10.2f}")
print(f"Price 2 is {price2:>10}")
print(f"Price 3 is {price3:<10}")