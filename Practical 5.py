import sys

def fib(n):
    i,j = 0,1
    for k in range(n):
        i,j = j,i+j
        yield i



def takeinput():
    print(f"\n\nEnter the number \n\n")
    num  = int(sys.stdin.readline().strip())
    return num

def main():
    print("\t\t\t PRACTICAL 5;\t\t\t")
    print("\n\n\n")
    print("\t\t Fibonacci Generator \t\t")
    print("\n\n")
    for i in range(int(input("Enter the number of test cases\n"))):
     print(f'\n\n TEST CASE {i+1}')
 
     num = takeinput()

     t = ['st','nd','rd']

     s = lambda i : t[i-1] if (i in [1,2,3]) else 'th'


     for i,j in zip(fib(num),range(1,num+1)):
        if i>num:
            break
        print('The {j}{s}  fibonacci number is {i}\n.'.format(j = j, s = s(j), i = i))
    print(''.center(80,'#' ))
    print('End of Practical 5:')



if __name__=='__main__':
    main()
