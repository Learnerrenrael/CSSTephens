import sys



def check_dups(a):
    l = {}
    for i in a:
        l[i] = l.setdefault(i,0)+1
    return {i:j for i,j in l.items() if j>1}
            
    
            
    







def takeinput():
    print(f"\n\n Enter elements separated by space \n\n")
    a  = map(str,input().split())
    return [*a]

def main():
    print("\t\t\t PRACTICAL 15;\t\t\t")
    print("\n\n\n")
    print("\t\t Duplicates Search \t\t")
    print("\n\n")
    for i in range(int(input("Enter the number of test cases\n"))):
     print(f"\n\nTEST CASE {i+1}")
     a = takeinput()
     if check_dups(a):
        print("The list has duplicates.")
        print(check_dups(a))
     else:
        print("The list has no duplicates.")
    



    print('\n\n')
    print(''.center(80,'#' ))
    print('\n\nEnd of Practical 15:')



if __name__=='__main__':
    main()
