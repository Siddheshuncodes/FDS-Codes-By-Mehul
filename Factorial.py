num = int(input("Enter the number: "))

choice = input("Enter 1 for for loop and 2 for while loop: ")

if choice == 1:

    fact = 1

    for i in range (1,num+1):

        fact = fact*i

    print("Factorial of a number is: ",fact)


else :

     j = 1
     fact1 = 1
     while j <= num:

           fact1 = fact1 * j
           j = j +1

     print("Factorial of a number is: ",fact1)