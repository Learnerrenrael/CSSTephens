import sys


def ispalind(s):
    s = s.lower()
    i = 0
    j = len(s)-1
    while i<j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True
            
            
    







def takeinput():
    print(f"\n\n Enter a string. \n\n")
    a  = input("")
    return a

def main():
    print("\t\t\t PRACTICAL 11;\t\t\t")
    print("\n\n\n")
    print("\t\t PALINDROME \t\t")
    print("\n\n")
    for i in range(int(input("Enter the number of test cases\n"))):
     print(f"\n\nTEST CASE {i+1}")
     a = takeinput()
     if ispalind(a):
         print(f"\n\t'{a}' is a palindrome.")
     else:
         print(f"\n\t'{a}' is not a palindrome.")



    print('\n\n')
    print(''.center(80,'#' ))
    print('\n\nEnd of Practical 7:')



if __name__=='__main__':
    main()
