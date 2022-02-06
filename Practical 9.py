import sys
import math


def sum1(n,k):
    if k=='o':
      return n**2
    else:
      return n*(n+1)


    







def takeinput():
    print(f"\n\nEnter the number \n\n")
    n  = int(input().strip())
    return n

def main():
    print("\t\t\t PRACTICAL 9;\t\t\t")
    print("\n\n\n")
    print("\t\t Sum of first n ODD/EVEN Numbers \t\t")
    print("\n\n")
    for i in range(int(input("Enter the number of test cases\n"))):
     print(f"\n\nTEST CASE {i+1}")
     n = takeinput()
     print(f"Sum of first {n} odd numbers",sum1(n,'o'))
     print(f"Sum of first {n} even numbers",sum1(n,'e'))


    print('\n\n')
    print(''.center(80,'#' ))
    print('\n\nEnd of Practical 9:')



if __name__=='__main__':
    main()
