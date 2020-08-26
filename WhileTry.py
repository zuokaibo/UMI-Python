# 5.2 Write a program that repeatedly prompts a
# user for integer numbers until the user enters
# 'done'. Once 'done' is entered, print out the
# largest and smallest of the numbers. If the
# user enters anything other than a valid number
# catch it with a try/except and put out an appropriate
# message and ignore the number. Enter 7, 2, bob, 10,
# and 4 and match the output below.

largest = None
smallest = None
while True:
    inputnumber = input("Enter a number: ")
    if inputnumber == "done": break
    try:
        num = float(inputnumber)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest = num
    if num >= largest :
        largest = num
    elif num <= smallest :
        smallest = num
def finish(largest,smallest):
    print ("Maximum is", int(largest))
    print ("Minimum is", int(smallest))
finish(largest,smallest)


