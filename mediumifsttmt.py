#grade of student based on marks
'''
marks = float(input("enter your marks:"))
if (marks <= 100  and marks>=90 ):
    print("Grade A") 
elif (marks <= 89 and marks>=80):
    print("Grade B") 
elif (marks <= 79 and marks>=70):
    print("Grade C")       
else:
    print("Fail") 
    '''
'''
#valid triangle or not
s1 = int(input("enter a first side:"))
s2 = int(input("enter a second side:"))
s3 = int(input("enter a third side:"))
if (s1 + s2 > s3  and s1 + s3 > s2 and s2 + s3 > s1  ):
    print("This is valid Triangle")
else:
    print("This is not valid Triangle")
'''
#greatest of three numbers
'''
num1 = float(input("enter a first  number:"))
num2 = float(input("enter a second number:"))
num3 = float(input("enter a third number:"))
if (num1 == num2 == num3 ):
    print("given numbers are equal")
elif (num1 > num2 and num1 > num3):
    print("num1")
elif (num2> num1 and num2 > num3):
    print("num2") 
else:
    print("num3")      
     '''
'''

#leap year

year=int(input("enter a year : "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"leap year")
else:
    print(year,"not a leap year : ")    

'''