import sys

def is_leap_year(year):
    ''' Input: Int
        Returns :Bool'''

    if (year%400==0) or ((year%100!=0) and (year%4==0)):
        return True
    else:
        return False



def takeinput():
    print(f"Enter the year \n\n")
    year  = int(sys.stdin.readline().strip())
    return year

def main():
    print("\t\t\t PRACTICAL 3;\t\t\t")
    print("\n\n\n")
    print("\t\t Leap Year Function\t\t")
    print("\n\n")
    for i in range(int(input("Enter the number of test cases\n"))):
     year = takeinput()


     if is_leap_year(year):
        print(f'The year {year}  is a Leap Year.')
     else:
        print(f'The year {year} is Not a Leap Year.')
     print('\n\n\n')



if __name__=='__main__':
    main()
