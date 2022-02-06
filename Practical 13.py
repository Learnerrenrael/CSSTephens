import sys



def read_file(a):
    dic = {}
    with open(a,'r') as f:
        h = f.read()
        for i in h:
            dic[i] = dic.setdefault(i,0)+1
    return sum([dic[i] for i in dic if i in ('a','e','i','o','u')])
            
    
            
    







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
     print(read_file(a))



    print('\n\n')
    print(''.center(80,'#' ))
    print('\n\nEnd of Practical 12:')



if __name__=='__main__':
    main()
