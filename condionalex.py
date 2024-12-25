# Basic Condition: Write an if-else statement that prints "Even" if the number is divisible by 2 
# and "Odd" otherwise.

n=10
if n%2==0:
    print("even")
else:
    print("odd")

# Nested If: Create a program that checks if a number is positive, negative, or zero
#  using nested if-else statements.

  

n=1
if n>0:
    print("number is positive")
elif n==0:
        print("number is zero")
else:
     print("number is negative")
        


# Comparing Two Numbers: Write an if-else statement that
#  compares two numbers and prints "First number is larger",
#  "Second number is larger", or "Both are equal".
firstnumber=int(input("enter first number :-"))
secondnumber=int(input("enter second number :-"))
if firstnumber > secondnumber:
     print("first number is larger")
elif secondnumber >firstnumber:
     print("second number is larger")
else:
     print("both are equal")
     
# # Grade Evaluation: Write an if-else statement to evaluate a student's grade based on their marks.
# #  If marks are greater than or equal to 90, print "A", 
# # 75-89 print "B",
# #  50-74 print "C", 
# # and below 50 print "Fail".
marks=int(input("enter your marks:-"))
if marks >=90:
     print("A")
elif 75 <= marks <=89:
     print("B")
elif 50<= marks <=74:
     print("C")
else:
     print("fail")
# # Grade Evaluation: Write an if-else statement to evaluate a student's grade based on their marks.
# #  If marks are greater than or equal to 90, print "A", 
# # 75-89 print "B",
# #  50-74 print "C", 
# # and below 50 print "Fail".

#and operator used
marks=int(input("enter you marks:- "))
if marks >= 90:
     print("A")
elif marks>= 75 and marks<=89:
     print("B")
elif marks>= 50 and marks<=74:
     print("C")
else:
        print("fail")




# Leap Year Check: Write a Python program using if-else to check if a given year is a leap year or not.
year=1900
if year %400==0:
  if year %100==0:
    if year %4==0:
     print("year is leap year ")
else:
     print ("year is not leap year")

 # Divisibility Check: Write a Python program that checks if a number is divisible by both 3 and 5 using an if-else statement.
number=int(input("enter your number:-"))
if number %3 ==0 and number %5==0:
     print("number is divisble by 3 and 5")
else:

     print("number is not divisble by a and 5")

# Temperature Advice: Write an if-else statement that suggests clothing based on temperature input.
#  If temperature is below 10°C, print "Wear a coat". 
# If temperature is between 10°C and 20°C, print "Wear a jacket". 
# Otherwise, print "Wear light clothing".
temp=11
if temp <10:
     print("wear a coat")

elif temp>=10 and temp<= 20:
     print("wear a jacket")
else:
     print("wear light clothing")

# Even or Divisible by 5: Write a program that checks if a number is even or divisible by 5 and prints the appropriate message using if-else.
num=int(input("enter you number:- "))
if   num%2==0 and  num%5==0 :
     print("number is even and divisible by 5")
else:
      print("number is not even and not divisible by 5")
# Ticket Pricing: Write a Python program that calculates the ticket price.
#  If age is less than 18, the price is $10, 
# if age is between 18 and 60, the price is $15, 
# and if age is over 60, the price is $8.
age=int(input("enter your age:- "))
if age<18:
     print("ticket price $10")
elif age >=18 and age <=60:
     print("ticket price $15")
else:
     print("ticket price $8")

     


