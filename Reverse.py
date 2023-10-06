num = int(input("Enter the number: "))

revno = 0

while num>0:
      rem = num % 10
      revno = (revno * 10) + rem
      num = num // 10

print("Reverse of number is: ", revno)