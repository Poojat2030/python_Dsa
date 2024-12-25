# if statement
# syntax:- if[condition expression]:
        #  [statement(s)to execute]

# # example
# a=11
# if a%2==0:
#       print("even number")

# if statement(the statement if are codition are right then they execute)
a=int(input("enter the value:- "))
if a%2==0:
     print(a,"even number")


#if else statemnt 

# syntax:- if[condition expression]:
        #   [statement to execute ]
#         else:
        #  [alternate statement to execute]

# example
# a=10
# if a%2==0:
#      print("even number")
    # else:
    # print("odd number")


a=int(input("enter the number :-"))
if a%2==0:
     print("even number")
     print("this number is the even number")
else:
     print("odd number")


    # if elif else statement
    # if[condition #1]:
        #   statement[#1]
    # elif[condition #2]:
        #   [statement #2]
    # elif[conditon #3]:
    #     [statement #3]
    # else:
        #   print("")


    # example
m=56
if m >= 60:
     print("first division")
elif m >= 48:
     print("second division")
elif m> 35:
     print("third dividion")
else:
     print("fail")

