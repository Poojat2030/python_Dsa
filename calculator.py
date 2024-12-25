print('''
 + add
 _-subtract
  *muliply
 /divide
     '''  )
num1=int(input("enter the value:1"))
num2=int(input("enter the value num:2"))
opr=input("enter the opr..  ")
if opr=="+":
    print(num1 + num2)
if opr=="-":
    print(num1-num2)
if opr =="*":
    print(num1*num2)
if opr=="/":
    print(num1/num2)
else:
    print("print invalid opr")
