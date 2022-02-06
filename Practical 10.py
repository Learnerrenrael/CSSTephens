import sys


def patter1(n):
    for i in range(1,n+1):
        for j in reversed(range(1,i+1)):
            print(j,end='')
        print()

def patter2(n):
    if (n==1):
        print("1\n1")
    for i in range(1,n+1):
        s = ''
        for j in range(1,i+1):
            s+=str(j)
        for k in reversed(range(1,i)):
            s+=str(k)
        if n>=10:
            print(s.center(4*n-20))
        else:
            print(s.center(2*n-1))
    for i in reversed(range(1,n)):
        s = ''
        for j in range(1,i+1):
            s += str(j)
        for k in reversed(range(1,i)):
            s += str(k)
        if n>=10:
         print(s.center(4*n-20))
        else:
         print(s.center(2*n-1))
    
            
    







def takeinput():
    print(f"\n\nEnter two numbers \n\n")
    a,b  = map(int,input().strip().split())
    return a,b

def main():
    print("\t\t\t PRACTICAL 10;\t\t\t")
    print("\n\n\n")
    print("\t\t PATTERNS \t\t")
    print("\n\n")
    for i in range(int(input("Enter the number of test cases\n"))):
     print(f"\n\nTEST CASE {i+1}")
     a, b = takeinput()
     print('Pattern 1 :')
     patter1(a)
     print('\n\n')
     print('Pattern 2:')
     patter2(b)
     


    print('\n\n')
    print(''.center(80,'#' ))
    print('\n\nEnd of Practical 10:')



if __name__=='__main__':
    main()
