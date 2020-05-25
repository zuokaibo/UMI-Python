# code 1
print('hello python from IntelliJ')
# here, you can add a new repo for new project, if you add a repo in github first,
# then you import this project to github by a command git remote set-url <new repo
# name> then git remote -v to check, then git pull origin master --allowed-unrelated-histories
# also, git clone new ssh, if you want to set up different repo for different projects




# code 2
x = 2
x = x + 2
print(x)
if x > 3:
    print('x is bigger than 3.')
print('x is smaller.')
if x > 8:
    print('it is a lie.')
print('ok, now it is working')
if x < 2:
    print('x<2')
elif x < 3:
    print('x<3')
else:
    print('x is 4')
print('all done')
# here, attention, if, elif and else, you can treat them as a big box, with many statement, if a statement is true, then
# no matter how many more true statement down below the first true statement, only the first statement would be executed.




# code 3
# person = input('Enter a number')
# # input is pop up statement, it will ask you to enter a number in terminal. becareful.
# try:
#     person2 = int(person)
#     print('it is a number')
# except:
#     person2 = -1
#     print('it is not a number')
# print('all done 1')
# here, we learnt try except statement to check some input code, becasue there are always
# some clients enter something not programmer expect.



# code 4
def greet(lang):
    if lang == 'en':
        print('I enter en')
    elif lang == 'es':
        print('I enter es')
    else:
        print('hello')
greet('en')
greet('bang')
# in this piece of code, we learnt define a definition. lang is a parameter, then
# we give it different argument, which are en and bang. then last two greet is invocation the def.



#  code 5
def addtwo(a, b):
    result = a+b
    return result
x = addtwo(5,6)
print(x)
# here, we practice def a function, and return statement, return determine the value in def definition.
# then we assign two numbers to the def function, and pass it to x,




# code 6
# here we learn while loop with break and continue, break is to break the loop, and jump out of the loop, while
# continue is jump to the top of loop, not break out of loop.
while True:
    result = input('> ')
    if result[0] == '#':
        continue
    if result == 'done':
        break
    # the first print statement will never execute, because it is unreachable, it is in while loop, if while trigger continue
    # then it jumps to the top of the loop, if break is triggered, it will jump out of loop, so, it is unreachable.
    print('we break the loop')
print('finally break the loop')