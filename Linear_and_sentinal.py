roll_list=[]

num = int(input("Enter the number of students: "))

for i in range(0, num):
    roll = int(input("Enter the roll no.: "))
    roll_list.append(roll)


def linear_search():

    count = 0
    value = int(input("Enter the roll no. to be searched: "))

    for i in range(num):
        if roll_list[i] == value:
            print("The value",roll_list[i],"is found at index no.:",i)
            count+=1

    if count==0:
        print("Roll no. does not exist")

def sentinal_search():

    value = int(input("Enter the roll no. to be searched: "))
    last = roll_list[num-1]
    roll_list[num-1]=value

    i = 0

    while(roll_list[i]!=value):
        i+=1

    roll_list[num-1] = last

    if(i<num-1 or roll_list[num-1]):
        print("The roll no. is present at",i,"position")
    else:
        print("The roll no. doest not exist")

        
while True:

    print(" 1.Linear Search\n 2.Sentinal Search\n 3.Exit")
    choice=int(input("Enter your choice: "))
    

    if choice == 1:

        linear_search()

    elif choice == 2:

        sentinal_search()

    elif choice == 3:

        break

