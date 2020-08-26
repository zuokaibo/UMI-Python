import math

def main():
    num = int(input("enter a number"))
    num = math.fabs(num)
    print(num)

# even you put print function in def, but because it is in Main(), so if you donot run Main()
#  nothing will be printed.
if __name__=="__main__":
    main()

