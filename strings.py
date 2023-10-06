def palindrome(str):
    rev=""
    for i in range(len(str),0,-1):
        rev = rev+str[i-1]
    if rev==str:
        print("The String is palindrome")
    else:
        print("The String is not palindrome")
        

def occurance(str):
    char=input("Enter the Char to be checked ")
    count=0

    for i in str:
        if char==i:
            count+=1

    print(count)
    print("The character",char,"is repeated",count,"times")

def longest(str): 

    str1=str.split(" ")
    print(str1)
    long_str= ""
    for i in str1:
        if len(i)>len(long_str):
            long_str=i

    print(long_str)

def frequency(str):

    str1=(str.split(" "))
    print(str1)
    new_list=[]
    for i in str1:
        if i not in new_list:
            new_list.append(i)

    print(new_list)

    for i in range(len(new_list)):
        print("Frequency of",new_list[i],"is: ",str1.count(new_list[i]))

def first_appear(str):

    sub_string = input("Enter the sub string to be found: ")

    str1=(str.split(" "))
    print(str1)
    new_list=[]

    for i in str1:
        if i not in new_list:
            new_list.append(i)

    print(new_list)

    
    for i in range(len(new_list)):
                
        if new_list[i] == sub_string:
        
            print("The first appearence of",new_list[i],"is at position",i)
               

while True:
      
    print(" 1.Palindrome\n 2.Occurance of each character\n 3.Word with longest lenght\n 4.Frequency of word\n 5.Index of first sub-string\n 6.Exit")
    choice = int(input("Enter your choice: "))
 
    if choice == 1:

        str = input("Enter the string: ")

        palindrome(str)

    elif choice == 2:

        str = input("Enter the string: ")

        occurance(str)

    elif choice == 3:

        str = input("Enter the string: ")

        longest(str)

    elif choice == 4:

        str = input("Enter the string: ")

        frequency(str)

    elif choice == 5:

        str = input("Enter the string: ")

        first_appear(str)

    elif choice == 6:

        break