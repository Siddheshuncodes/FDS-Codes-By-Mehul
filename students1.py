
num = int(input("Enter the total number of students: "))
mark_list= []

for i in range(0, num):
    mark = input("Enter marks: ")
    mark_list.append(mark)

def avg():

    sum=0
    avg = 0
    for i in range(len(mark_list)):
       if mark_list[i] != "a":
           sum = sum+int(mark_list[i])

    avg = sum/num       
    print("The average is: ",avg)

def absent():

    choice = 0
    for i in range(len(mark_list)):
       if mark_list[i] == "a":
           choice = choice+1

    print("Total number of absent students are: ", choice)       

def low_mk():
 
    low = mark_list[0]
    if mark_list[0] == "a":
       low = mark_list[1]
       for i in range(len(mark_list)):
           if int(mark_list[i] == "a"):
              continue
              if int(low)>int(mark_list[i]):
                   low = int(mark_list[i])

           elif int(mark_list[i] != "a"):
                if int(low)>int(mark_list[i]):
                   low = int(mark_list[i])

       print("The lowest marks is: ",low)

    elif mark_list[0] != "a":
        for i in range(len(mark_list)):
           if int(mark_list[i] == "a"):
              continue
              if int(low)>int(mark_list[i]):
                 low = int(mark_list[i])

           elif int(mark_list[i] != "a"):
                if int(low)>int(mark_list[i]):
                    low = int(mark_list[i])
         
        print("The lowest marks is: ",low)       


def high_mk():

   high = mark_list[0]
   if mark_list[0] == "a":
      high = mark_list[1]
      for i in range(len(mark_list)):
          if int(mark_list[i] == "a"):
             continue
             if int(high)<int(mark_list[i]):
                high = int(mark_list[i])
      print("The highest marks is: ",high)    

   elif mark_list[0] != "a":
        for i in range(len(mark_list)):
           if int(mark_list[i] == "a"):
              continue
              if int(high)<int(mark_list[i]):
                 high = int(mark_list[i])
           elif int(high)<int(mark_list[i]):
                high = int(mark_list[i])
     

        print("The highest marks is: ",high)       




while True:
      
    print(" 1.Average\n 2.Students absent\n 3.Lowest marks\n 4.Highest marks\n 5.Marks with highest frequency")
    choice = int(input("Enter your choice: "))
 
    if choice == 1:

       avg()

    elif choice == 2:
         
        absent()

    elif choice == 3:

        low_mk()

    elif choice == 4:

        high_mk()




