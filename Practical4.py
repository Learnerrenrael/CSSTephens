import sys

def factorial(n):
    '''Input : Int
       Returns : Int'''
    i = 1
    if n==0:
        return i
    while n:
        i*=n
        n-=1
    return i


def takeinput():
    factor = int(sys.stdin.readline().strip())
    return factor

def main():
    print("\t\t\t PRACTICAL 4;\t\t\t")
    print("\n\n\n")
    print("\t\t Factorial Function\t\t")
    for i in range(int(input("Enter the number of test cases\n"))):
     print(f"Enter a non-negative integer separated by space.\n\n")
     factor = takeinput()
     print("\n\n")
     print(f"The factorial of {factor} is {factorial(factor)}.")


if __name__=='__main__':

    main()

