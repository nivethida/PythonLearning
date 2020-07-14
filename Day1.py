# -*- coding: utf-8 -*-

#variables

 # text data type
 # x='hello world'
 # print(type(x))
 # 
 # # integer data type
 # x=5
 # print(type(x))
 # 
 # # float data type
 # x=5.5
 # print(type(x))
 # 
 # # boolean data type
 # x=True
 # print(type(x))
 # 
 # # most common operations
 # x=5
 # print(x/5)
 # print(x*5)
 # print(x+x)
 # print(x-x)
 # print(x**2) # this is power function in python
 # y=-5
 # print(abs(y)) # calcualte absolute value
 # 
 # # concatenation in print function
 # print("Were" + "wolf")
 # print("Door" + "man")
 # print("4" + "chan")
 # print(str(4) + "chan") # the str() method convert viable variables to a string
 # print(4 * "test") # repeating
 # 
 # # input value/parameter through console
 # name = input("Give me your name: ")
 # print("Your name is " + name) # this is how to concatenate strings in python

# calculate area of circle given input radius
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
integer=input('please enter the integer:')
a=int(2*str(integer))
b=int(3*str(integer))
value=int(integer)+a+b
print(value)

print(type(a))
print(type(b))
print(type(integer))
print(type(value))
# concerning variable names
# you cannot name a variable after a built-in function name, or built-in variable name.
#class=5 # syntax error, class is a built-in method
# try not to use special characters, they usually have other meanings.
field$=5 # invalid syntax

----------------------------------------------------------------------------------------
2. logical operation

# logical value generated from comparison
x=1
print(x>0)

y=2>1
print(y)

x=2
y=2
z=3
print(x==y)
print(x==z)

s=True & False
print(s)

t=(2>1)&(3>2)
print(t)

w=True | False
print(w)

u=(2>1)|(3>4)
print(u)
----------------------------------------------------------------------------------------
3. the datetime package

# get current datetime object
import datetime
datetime_object = datetime.datetime.now() # the first datetime if the package name, or the module name, the second datetime is the class called datetime inside the datetime module
print(datetime_object)

# get current date
import datetime
date_object = datetime.date.today()
print(date_object)

# convert input to date
import datetime
year=2019
month=4
day=13
d=datetime.date(year,month,day)
print(d)

# directly import the date method from datetime package
from datetime import date
year=2019
month=4
day=13
d=date(year,month,day)
print(d)

# convert unix timestamp to human time
from datetime import date
timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)

# extract only the year, the month, and the day from date object
from datetime import date
today = date.today() 
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

# the time method
from datetime import time

a = time() # equivalent to time(hour = 0, minute = 0, second = 0)
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# the same output
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

# extract the hour, minute, and second from time object
from datetime import time
a = time(11, 34, 56)
print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)

# the datetime method
from datetime import datetime
a = datetime(2018, 11, 28)
print(a)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)

# extract details from datetime object
from datetime import datetime
a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

# timedelta method, to calculate the different between two datetime
from datetime import datetime, date
t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)
t4 = t2 - t1
print("t4 =", t4)
print(t4.days)
print(t4.total_seconds()) # the total seconds between two dates, seconds itself doesn't work
----------------------------------------------------------------------------------------
4 the numpy package

# numpy is a library for scientific computing in Python. It provides a high-performance multidimensional array object.
# it is very convinient to do linear algebra with numpy arrays

import numpy as np

# defining one dimension array
array1=np.array([1,2,3,4,5,6])
print(array1)

# defining two dimensional array, you can see this as a matrix
array2=np.array([[1,2,3],[3,2,1]])
print(array2)

# shape of array
print(array2.shape)

# generate zero arrays of some array's shape, usually used for initialization
print(np.zeros(array2.shape))

# changing elementin array
array1[0]=9
print(array1)
array2[0,2]=9 # the first row, the third column
print(array2)

# create identity matrix
array3=np.eye(4) # 4 is the size of the identity matrix
print(array3)

# creating random number
import numpy as np
rand1=np.random.rand() # a random number between 0 and 1
print(rand1)

rand2=np.random.rand(2,3) # generate a random matrix with size 2 by 3
print(rand2)

rand3=np.random.randn(5) # generate 5 standard normally distributed numbers 
print(rand3)

import numpy as np
rand4=np.random.randint(4,size=(2,4)) # random draw a matrix of desired size using random integers from 1 to 4
print(rand4)

import numpy as np
rand5=np.random.randint(5,10,size=(2,4))
print(rand5)

# arithemetic operations
array1=np.array([[1,2,3],[3,2,1]])
array2=np.array([[0,0,0],[1,1,1]])
print(array1+array2) # elementwise arithmetic operation
print(array1*array2)
#print(array1/array2) # will be error 
print(array1-array2)

# matrix multiplication
a=np.array([[1, 0],
            [0, 1]])
print(a)
b=np.array([[1,2],
            [3,4]])
print(b)
print(np.matmul(a,b))
c=np.array([1,2])
print(np.matmul(c,b)) # this is the normal matmul
print(np.matmul(b,c)) # because b is 2*2, c is 1*2, this should not work, but np automatically transpose c to a 2*1 array

 