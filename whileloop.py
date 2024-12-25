# while loop in python
# start
# condition
# increment/decrement
i=1
while i<=10:
    print(i,"welcome the loops")
    i+=1
print(i)
# reeverse
i=10
while i >= 1:
    print(i,"welcome to loops")
    i=i-1
    print(i)


# new apana college
# loops are used to repest condtion
# while condtion 
# some work
count=1
while count<= 5:    
    print("hello")
    count +=1
print(count)

# print numbers 1 to 100
number=1
while number <=100:
  print("number")
  number+=1
  print(number)

# print numbers 100 to 1
i=100
while i>=1:
    print(i)
    i=i-1

# print multiplication table of a number n.
i=1
while i<=10:
    print (i*3)
    i+=1

# print the elements of the following list using a loop
[1,4,9,16,25,36,49,64,81,100]
nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1

    # search for a number  x in the tuple using loop
    #  (1,4,9,16,25,36,49,64,81,100)
nums=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i<len(nums):
    if(nums[i]==x): 
      print("found at idx",idx)
    i+=1


# two keywords in loop 1] break 2] continue
# 1] break-used to terminate the loop when encounterd

i=1
while i<=5:
    print(i)
    if i==3:
       break
i+=1
print("end of loop")

# 2] continue-terminates execution in the current iteration &continues execution of loop with the nex iteration
i=0
while i<=5:
    if(i==3):
        i+=1
        continue #skip
    print (i)
    i+=1



    #   wap to find the sum of first n number (suing while)


