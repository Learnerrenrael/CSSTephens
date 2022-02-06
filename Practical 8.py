import sys
import math


def is_prime(n):
    if (n ==2) or (n==3):
        return True
    elif (n == 1):
        return False
    elif (n%6 == 1) or (n%6==5):
        for i in range(2,math.floor(math.sqrt(n))+1):
            if (n % i) == 0:
                return False
        return True
    else:
        return False
    







def takeinput():
    print(f"\n\nEnter the number \n\n")
    n  = int(input().strip())
    return n

def main():
    print("\t\t\t PRACTICAL 8;\t\t\t")
    print("\n\n\n")
    print("\t\t Prime Checker \t\t")
    print("\n\n")
    for i in range(int(input("Enter the number of test cases\n"))):
     print(f"\n\nTEST CASE {i+1}")
     n = takeinput()
     if is_prime(n):
         print(f"The given number {n} is a prime number")
     else:
         print(f"The given number {n} is not  a prime number")
         


    print('\n\n')
    print(''.center(80,'#' ))
    print('\n\nEnd of Practical 8:')



if __name__=='__main__':
    main()
