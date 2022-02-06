import sys



def read_file(a):
    dic = {'a':0,'e':0,'i':0,'o':0,'u':0}
    with open(a,'r') as f:
        h = f.read()
        for i in h:
            if i in ('a','e','i','o','u'):
              dic[i] = dic[i]+1
    return dic
            
    
            
    







def takeinput():
    print(f"\n\n Enter the absolute path of the file. \n\n")
    a  = input()
    return a

def main():
    print("\t\t\t PRACTICAL 12;\t\t\t")
    print("\n\n\n")
    print("\t\t File Search \t\t")
    print("\n\n")
    for i in range(int(input("Enter the number of test cases\n"))):
     print(f"\n\nTEST CASE {i+1}")
     a = takeinput()
     print("The frequency of vowels in the text\n")
     print(read_file(a))



    print('\n\n')
    print(''.center(80,'#' ))
    print('\n\nEnd of Practical 12:')



if __name__=='__main__':
    main()
