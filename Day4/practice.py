# -*- coding: utf-8 -*-


thesum = 0
for i in range(2,25):
    print(i)
    if i% 5 == 0:
        break
    thesum+=i
print(thesum)    
    
for i in "35":
    print(i)    
    
    
def func(*args):
    n = sum(args)
    while abs(n) > 9:
        print(n, "n1")
        p = 1
        for i in str(n):
            print(i, "i", n )
            p*=int(i)
            print(p, "p")
        n = p
        print(n, "N")
    return n

print(func(15,20))    

import pandas as pd
 
# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']
 
# Calling DataFrame to make the list a dataframe
df = pd.DataFrame(lst)
print(df)

data = [[1,2,3,4,5],[6,7,8,9,10]]

df2 = pd.DataFrame(data)

print(df2)

import pandas as pd
data1 = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]} # the column names are already included.
df4 = pd.DataFrame(data1)
print(df4)

import pandas as pd
data3 = {'Name':['A', 'B', 'C', 'D'],
        'Age':[27, 24, 22, 32],
        'Address':['W', 'A', 'S', 'D'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df5 = pd.DataFrame(data3)
print(df5) # print the full dataset
# select two columns using column names
print(df5[['Name', 'Qualification']])
print(df5['name'])# this is a series if you check print(type(df['name']))
print(df5[['name']]) # this is a dataframe, again, you can check the data type
name1=df5['Name']
name2=df5[['Name']]
print(name1[0]) # this is atomic value "A"
print(name2.iloc[2]) # this is a series
# but if you want to get two columns you need print(df[['Name', 'Qualification']]).

x = 1
while x < 5:
    print(x)
    x = x + 1

x = 1
while True:
    print(x)
    x = x + 1
    if x >= 5:
        break

for i in range(1,5):
    print(i)
    print("cheers!")


x = [1,3,4,5]
for i in x:
    if i > 2:
        print(i)



import pandas as pd
data23 ={'Name':['Tom','nick','krish','jack'],'Age':[20, 21, 19, 18]}
df45=pd.DataFrame(data23)
print(df45)
print(df45.iloc[:,0])
print(df45.iloc[0,:])
df13=df45.loc[df45['Age']<20,:]
print(df13)


for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print('Current Letter :', letter)

var = 10
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print('Current variable value :', var)
print("Good bye!")


x=['1st entry','2nd entry']
for i,entry in enumerate(x):
     print(i) # the index of iteration we are currently at
     print(entry) # the iterator

f=[x for x in range(1,10)]
print(f)

for x in range(1,4):
    print(x)

g=[(x,y) for x in range(1,4) for y in range(5,7)]
print(g)
    
r=[(x,y) for x in range(1,4) for y in range(x+1,x+3)]
print(r)

h=[(y,x) for y in range(5,7) for x in range(1,4)]
print(h) # for each y, populates all possible x


i=[{'key {}'.format(y):x} for x in range(4,6) for y in range(1,3)]
print(i)


x=[1,2,3]
y=[4,5,6]
z=[x/y for x,y in zip(x,y)]
print(z)

tuple_list=[(1,2),(3,4),(5,6)]
j=[(x**2+1,y) for (x,y) in tuple_list]
print(j)

dictionary={'color':'yellow','num_core':8,'ram':16}
print(dictionary)

for i in dictionary:
     print('the',i,'is',dictionary[i])

word='success' 
dictionary1={} # define an empty dictionary, get ready for entries.
for c in word:
     if c not in dictionary1: # if the dictionary has not pick up the key
          dictionary1[c]=1 # create the key and set the value to 1 because this is the first occurrence
     else: # if the dictionary has already picked up the key
          dictionary1[c]=dictionary1[c]+ 1 # add 1 to the current value due to another occurrence.
print(dictionary1)



d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)


my_dict = {'data1':100,'data2':-54,'data3':247}
result=1
for value in my_dict.values():    
    result *= value
print(result)


import numpy as np
rand5=np.random.randint(2,10,size=(2,4))
print(rand5)

x=[54,12,32,41,33]
y=[1,2,3,4]
for i in zip(x,y):
    print(i)    

import pandas as pd
data = {'Name':['A', 'B', 'C', 'D'],
        'Age':[27, 24, 22, 32],
        'Address':['W', 'A', 'S', 'D'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df = pd.DataFrame(data)
print(df) # print the full dataset
# select two columns using column names

name1=df['Name']
name2=df[['Name']]
print(name1,'series')
print(name2,'df')
print(name1[0]) # this is atomic value "A"
print(name2.iloc[2]) 



from datetime import datetime
now = datetime.now()
year = now.strftime("%Y")
print("year:", year)
month = now.strftime("%m")
print("month:", month)
month = now.strftime("%B")
print("month:", month)
time = now.strftime("%H:%M:%S")
print("time:", time)
time = now.strftime("%I:%M:%S %a")
print("time:", time)

import random
print(random.uniform(5, 100))

import numpy as np
print(np.random.randn(5))
print(np.random.randn(5,2)) 


x=[54,12,32,41,33]

print(x[1:3]) 


x = 5
y = 1

p = y/x if y>=x else "lower vaue"
print(p)


for i in range(3):
    print(i)



def charcount(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i,0)+1
    return dict

print(charcount("error"))    


str1 = "asfgthfs"
str2 = "12345677"

dict1 = dict(zip(str1,str2))

print(dict1)

dict2 = {}

print(type(dict2), len(dict2))


import statistics
x=[1,2,3,4,5,6,7,8]

for i in x[:3]:
    print(i)
    
for i in x[-3:]:
    print(i)    
print(statistics.mean(x[:3]))

print(statistics.mean(x[-2:]))

list1 = [1,2,3,4,5,6,7,8]

result = ["Even" if x%2==0 else "Odd" for x in range(1,10)]

print(result)


ar1 = [1,5,10,20,40,80]
ar2 = [6,7,80,100]
ar3 = [3,4,15,20,30,70,80,120]

def function(*thelist):
    outputset = set(thelist[0])
    for i in thelist:
        
        outputset = outputset & set(i)
        print(outputset)
    return outputset

print(function(ar1,ar2,ar3))    


def function1(list1, N):
    final_list = []
    for i in range(0,N):
        max1 = 0
        for j in range(len(list1)):
            print(len(list1))
            if list1[j] > max1:
                max1 = list1[j];
        list1.remove(max1);
        final_list.append(max1)
    print(final_list)
print(function1([1,2,3,4,5,6],3))     


var = 9
while var%2==1 and var>=0:
    var = var-2
    if var == 4:
        continue
    print(var)

x=[56,32,21,8,56,21,35]
print(x[:2])
for index,value in enumerate(x):
    if value in x[:index]:
        print(x[:index])
        print(value,index)


Keys=['length','width','depth','weight','reliability']
Values=[6,7,8,9,'good']

dict4 = {x:y for x,y in zip(Keys,Values)}
print(dict4)
print(dict4.get('width', 'feature not found'))

unique={}
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
unique.update(d1)



L1 = list() 
L1.append([1, [2, 3], 4]) 
L1.extend([7, 8, 9]) 
print(L1)
print(L1[0][1][1] + L1[2])



l=[1,2,3,4]

print(l.index(1))







