import sys


def lcm(a,b):
    prod = a*b
    if prod == 0:
        return 0
    else:
        return (a*b)/gcd(a,b)

def gcd(a,b):
    a,b = max(abs(a),abs(b)), min(abs(a),abs(b))
    while b!=0:
        a,b = b,a-(a//b)*b
    return a
    







def takeinput():
    print(f"\n\nEnter two numbers \n\n")
    a,b  = map(int,input().strip().split())
    return a,b

def main():
    print("\t\t\t PRACTICAL 7;\t\t\t")
    print("\n\n\n")
    print("\t\t LCM calculator \t\t")
    print("\n\n")
    for i in range(int(input("Enter the number of test cases\n"))):
     print(f"\n\nTEST CASE {i+1}")
     a, b = takeinput()
     print(lcm(a,b))


    print('\n\n')
    print(''.center(80,'#' ))
    print('\n\nEnd of Practical 7:')



if __name__=='__main__':
    main()
