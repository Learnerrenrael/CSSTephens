
"Functions that output number patterns"

def pattern1(n):
    i = 1
    while i<=n:
        print('\t'*2,end='')
        j = 0
        k = i
        while j<n-i:
            print(' ', end='')
            j+=1
        while k >=1:
            print(k,end=' ')
            k-=1
        print()
        i+=1

def pattern2(n):
    i = 1
    r = 1
    while i<=n:
        print('\t'*2,end='')
        l=0
        j = 1
        k = i-1
        while l<=n-i:
            print('  ',end='')
            l+=1
        while j<=i:
            print(j,end=' ')
            j+=1
        while k>=1:
            print(k,end=' ')
            k-=1
        print()
        i+=1

    while r<=n-1:
        print('\t'*2,end='')
        h = 0
        t = 1
        p = n-r
        while h<=r:
            print('  ',end='')
            h+=1
        while t< n-r:
            print(t, end=' ')
            t+=1
        while p>=1:
            print(p,end=' ')
            p-=1
        print()
        r+=1
            
        
        



    
if __name__=='__main__':
    print(f'Write a python function to produce above outputs for any number n  : \n\n'
          f'\t\t{pattern1(4)} \n\n {pattern2(5)}\n\n')
   
    a,b = list(map(int,input("Enter a,b seperated by space below:\n").strip().split()))
    print('\t\t\tPattern1\n\n')
    pattern1(a)
    print('\n\n\t\tEnd of Pattern1\n\n')
    print('*'*75+'\n\n')
    print('\t\t\t\tPattern2\n\n')
    pattern2(b)
    print('\n\n\t\t\tEnd of Pattern2')
    print('*'*75+'\n\n')
    
