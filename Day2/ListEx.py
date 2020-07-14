# -*- coding: utf-8 -*-

a = ['first','second','third','four']

"length"
print(len(a))

"index"
print(a[0], a[1])

print(a[0:2])

"extracting a part from a long list"
print(a[:2])

"extracting last element"
print(a[len(a)-1]) #not recommended

print(a[-1])

"last two elements"
print(a[-2:])

print(a[0]*4)

"inserting values"
x = []

x.append(1)

print(x)

x.append(2)

x.append(3)#appends at the end


x.pop()# pops at the end

print(x)

y = [1,2,3,4,5] # at any point

y.insert(0,6)
print(y)

"concatenation"

z = [1,32,453]

i = [8894,'dhd','dhd']

j = z+i
# j =z.extend(i)
"important"

print(j)

"updating values in list"
var1 = [1,2,3]

var1[1] = -1
var1[2] = -9

"sum of the list"

b = [1,2,3,4,5,2]

print(sum(b), max(b), min(b))

import statistics as stat

print(stat.mean(b), stat.median(b), stat.mode(b), stat.stdev(b))


k = [2,5,6,7]
l = [9,45,78]

for i in zip(k,l):
    print(i)
    
var3 = 10
if var3>10:
    print('large')
else:
    print('small')
    

userinput = input('please enter a number')

if userinput .isdigit():
    userinput = float(userinput)
    if userinput>10:
        userinput-=1
    else:
        userinput+=123
    print(userinput)    
else:
    print('Please enter a number')
    

hardware_skill = True
software_skill = False    

if hardware_skill and software_skill:
    print('excellent')
elif hardware_skill or software_skill:
    print('good')
else:
    print('insufficient')    
    

"in line if statement"
h = 3

h = h/2 if h%2 == 0 else h

print(h)

userinput2 = input('please enter a month')
if userinput2 == 'February':
    print('28 or 29 days')
elif userinput2 in ['January', 'March', 'May', 'July', 'August', 'October', 'December']:
    print('31 days')
else :
    print('30 days')
    
 
 