# prime number
number=int(input("Enter a number: "))
flag=False
if number=1:
  print(number,"is not a prime number")
elif number>1:
  for i in range(2,number):
    if(number%i)==0:
      flag=True
      break
  if flag:
    print(num,"is not a prime number")
  else:
    print(num,"is a prime number")
    
# python program to display all the prime numbers within an interval
number1=int(input("Enter number1: "))
number2=int(input("Enter number2: "))
print("Prime numbers between",number1 , "and", upper, "are: ")
for num in range(number1,number2+1):
  if num>1:
    for i in range(2,num):
      if(num%i)==0:
        break
      else:
        print(num)
        
