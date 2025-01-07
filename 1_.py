# Methods, Help & Documentation Practice #1
# Remove the characters to the left of our main text:

# ,

# :

# %

#into reuseable units

#how you define a function
#only define the function ONCE
#whatever I pass inside the parentheses
#is called a parameter
# a parameter is a placeholder for future information
# def sayHello(name,age,address):
#     print(f'say Hello{name}')
#     print(f'Hello Governor, your address is {address}')
#     print(f'welcome back{name}')
#     print(f'your age is{age}')
# #once you define a function
# #you must call or invoke the function
# #when I pass in information ihe function
# #the called function, its called an argument
# sayHello('Pancho',34, "234 yo mama ave")
# sayHello("Pablo",25,'221 yo mama ave')
# sayHello('Freakbob',45, '225 yo mama ave')


# def determinEligibility(age):
#     #if your age is over 18, you can vote,
#     #otherwise you cant
#     if age >= 18:
#         print('you can vote')
#     else:
#         print('you have to wait')

# determinEligibility(12)
# determinEligibility(15)
# determinEligibility(19)

# def willYouGraduate(gpa,credits,SAT):
#     #gpa : number variable
#     #credits: number variable
#     #pass SAT :BOOLEAN
#     if(gpa == 3.0) and (credits>= 28) and (SAT == True):
#         print('you passed. Good luck in college')
#     elif (gpa < 3.90) or (credits < 28) or (SAT != True):
#         print('back to the drawing board')
#     else:
#         print('talk to your counselor')


# willYouGraduate(2.8,15,True)
# willYouGraduate(4.0,30,True)
# willYouGraduate(3.0,28,False)

#return = statment used to end a function and send a result back to the caller


# def add(x,y):
#     z = x + y
#     return z

# def subtract(x,y):
#     z = x - y
#     return z

# def multiply(x,y):
#     z = x * y
#     return z

# def divide(x,y):
#     z = x / y
#     return z

# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide(1,2))

def creat_name(firts, last):
    first= first.capitalize()
    last= last.capitalize()
    return first + " " + last