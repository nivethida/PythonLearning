# -*- coding: utf-8 -*-
x = 1
while True:
    x+=1
    if x>5:
        break
    print(x)
    

for i in range(1,5):
    print(i)

for i in [1,2,3,4,5]:
    if i>2:
        print(i)
        
x = [42,23,22,32,62,12]

temp_large = x[0]

for i in x:
    if temp_large < i:
        temp_large=i

print(temp_large)        

            
x = 'python'
for i in x:
    if i == 'h':
        continue
    print(i)           


x = [12,22,33,43,52,63,65]

odd_no = []
even_no = []

for i in x:
    if i%2 == 0:
        odd_no.append(i)
    else:
        even_no.append(i)
        
print(odd_no)        
print(even_no) 


#count the number of integers between 1500 and 2700 if
#that integer can be divided by 5 and 7

counter = 0

for i in range(1500,2700):
    if i%5 == 0 and i%7 == 0:
        counter+=1

print(counter)


import string
print(string.punctuation)
letter = ''
digit = ''
punc = ''
x = 'python3.0'

for i in x:
    if i.isdigit():
        digit+=i
    elif i in string.punctuation:
        punc+=i
    elif i.isalpha:
        letter+=i
        
print(letter)
print(digit)
print(punc)        
    
    

x = input("please enter a number:")

for i in range(1,11):
    print(x, "x", i, "=", int(x)*i)
    

for i in range(1, 10):
    print(str(i)*i)   
    


x = [1, 25, 8 ,0]

y = [2, 4, 25, 0]

for i in x:
    for i in y:
        print(i)
    
x = set(x)
y = set(y)

print(x|y)

#print(set(x+y))

x = ['1st entry', '2nd entry']

for index, value in enumerate(x):
    print(index, value)
    
#########################################
    
x = ['apples', 'bananas', 'oranges']

for index, value in enumerate(x):
    print('the {}th fruit is {}'.format(index,value)) # print('the %dth fruit is %s' % (index,value))    
   


#########################################
    
    
x = [1, 25, 9, 8]

y = [25, 10, 1, 18]

common = [i for i in x if i in y]

print(common)

x = 'python3.0'

letter = [x for x in x if x.isalpha()]

print(letter)

g = [(x,y) for x in range(1,4) for y in range(5,7)]
print(g)

#for x in range(1,4):
#    for y in range(5,7):

g = [{'key {}'.format(x):y} 
      for x in range(1,3)
      for y in range(3,5)]
print(g)

tuple_list = [(1,2), (3,4), (5,6)]

print([(x**2, y) for (x,y) in tuple_list])


x = [10,222,333]
y = [4,5,6]

z = [i%j for (i,j) in zip(x,y)]

print(z)


keys=['weight', 'height', 'depth', 'length', 'width']

values = [1, 2, 3, 4, 5]

output = [{'{}'.format(key):value} for key, value in zip(keys, values)]

print(output)


#####################################ROCK PPAPER SCISSORS

import random
space = ['rock', 'scissors', 'paper']

user_choice = input("please make your choice")

sys_choice = random.sample(space, 1)[0]

while user_choice == sys_choice:
    user_choice = input("tie, enter again")
    sys_choice = random.sample(space, 1)[0]

#tie breaks

if space.index(user_choice) < space.index(sys_choice) or (user_choice == 'paper' and sys_choice == 'rock'):
    print("you win")
else:
    print("you lose")
    
    

    
     






































        