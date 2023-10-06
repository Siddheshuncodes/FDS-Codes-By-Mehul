num = int(input("Enter a number: "))

for i in range (1,num+1):

    res = i % 2

    if res == 0:

        print("Number",i, "is Even")

    else:

        print("Number",i, "is Odd")