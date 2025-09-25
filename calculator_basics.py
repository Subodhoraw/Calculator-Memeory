#create a simple calculator with addition, subtraction, multiplication, and division functions
# 10 steps to build a calculator 
#1.define the functions
#2.get user input   
#3.call the functions with the user input
#4.display the results
#5.handle errors (e.g., division by zero)
#6.add a loop to allow multiple calculations
#7.add a way to exit the program
#8.format the output for better readability
#9.add comments to explain the code
#10.test the calculator with different inputs

def add( num1, num2):
    return num1+ num2
#subtraction function
def subtract(num1, num2):
    return num1 -num2
#multiplication function
def multiply(num1,num2):
    return num1*num2
#division function
def divide(num1,num2):
    if num2 == 0:
        return "Error! division by zero."
    return num1/num2
def avg(num1,num2):
    return (num1+num2)/2

#step 2: get user input
print("please select operation:\ "\
      "1.addition\n"\
     "2.subtraction\n"\
     "3.multiplication\n"\
     "4.division\n"\
     "5.average\n")

select = int(input("select operation(1/2/3/4/5):"))
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))

#step 3: call the functions with the user inputid
if select == 1:
    print(num1,"+",num2,"=",\
          add(num1,num2))
elif select == 2:
    print(num1,"-",num2,"=",\
          subtract(num1,num2))  
elif select == 3:
    print(num1,"*",num2,"=",\
          multiply(num1,num2))
elif select == 4:
    print(num1,"/",num2,"=",\
          divide(num1,num2))
elif select == 5:
    print("average of",num1,"and",num2,"is",\
          avg(num1,num2))
else:
    print("invalid input! PLEASE SELECT A VALID OPERATION")


