#typecasting

name ="name"
age=30
gpa=3.2
is_student=False

gpa=int(gpa)

print(type(gpa))

#input

userInputName = input("What is your name?: ")
userInputAge = int(input("What is your age?: "))
userInputAge+=1
print(userInputAge)
print(userInputName)



#madlibs game

adjective1 = input("Enter an adjective (desc): ")
noun1 = input("Enter a noun (person,place etc): ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}.")
