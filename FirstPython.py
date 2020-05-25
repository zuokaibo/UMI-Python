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
# while True:
#     result = input('> ')
#     if result[0] == '#':
#         continue
#     if result == 'done':
#         break
#     # the first print statement will never execute, because it is unreachable, it is in while loop, if while trigger continue
#     # then it jumps to the top of the loop, if break is triggered, it will jump out of loop, so, it is unreachable.
#     print('we break the loop')
# print('finally break the loop')



# code 7
# here we learn for loop, which is used to iterate all values in a list of string,
friends = ['Jordan', 'Bo','Mimi', 'Fen']
for onefriend in friends:
    print('Hello, my friend,', onefriend, ', I am learing for loop')
print('loop four times')



# code 8
# here we learn how to find the largest number in a list of numbers.
largestsofar = -1
for num in [12, 34, 23, 98, 44, 66]:
    if num > largestsofar:
        largestsofar = num
        print ('largestsofar is ', largestsofar)
print('so far, the largest number is ', largestsofar)


# code 9
# here we need to find the smallest number in the list of number, can we set a number to smallestsofar? what number should
# that be if we donot know the list of numbers, or there are billions of number in the list?
# here, we use None, also, assign it by "is"
smallsofar = None
for newnum in [12, 45, 67, 23, 3, 7]:
    if smallsofar is None:
        smallsofar = newnum
#       this if statement is absolutely right for first time of looping.actually, this first time of loop is
#     to assign the fisrt number in the list to the smallsofar variable. then compare it to the rest of list.
#     in the statement below, is to compare the first number in the list to the rest numbers one by one, if there is
#     a smaller one then the first number, then assign samller number to the smallsofar.
    elif newnum < smallsofar:
        smallsofar = newnum
        print ('samllsofar', newnum)
print ('smallest number so far is ', smallsofar)


# code 10
# here we lear to count a list of number.
count = 0
for num1 in [12, 24, 35, 46, 57]:
    count = count +1
    print(count, num1)



# code 11
# here we do sum
sum = 0
for num2 in [12,13,14,15,18,17,16,15]:
    sum = sum + num2;
    print ('sum now is: ', sum)
