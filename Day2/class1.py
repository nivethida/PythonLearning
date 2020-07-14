# -*- coding: utf-8 -*-

"Given a list x, write code to print True if the first element of the list is equal to the last element of the list, and print False otherwise."

list1 = ['2', '3', '5', '8']

if list1[0] == list1[-1]:
    print(True)
else:
    print(False)
    


list2 = [1, 3, 4, 5, 6, 7, 1, 3, 4]

import statistics as stat

first3 = list2[0:3]
print(first3)
last3 = list2[-3:]
        
if stat.mean(first3) == stat.mean(last3):
    print('Yes')
else:
    print('No')    
    
    

data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}

"Please" 
"   •	extract the first column"
"	•	extract the first row"
"	•	extract a sub data frame for those who are under 20"

import pandas as pd

df1 = pd.DataFrame(data)

df2 = df1[['Name']]

print(df2)

df3 = df1.iloc[0] 

print(df3)

print(df1.loc[df1['Age']<=20])


triangle = [60,30,30]

if triangle[0] == triangle[1] == triangle[2]:
    print('Equilateral triangle')
elif triangle[0] == triangle[1] or triangle[0] == triangle[2] or triangle[1]==triangle[2]:
    print('isosceles triangle') 
else:
     print('scalene triangle') 