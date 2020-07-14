dictionary = {'color':'yellow', 'num_core': 8}

print(dictionary['color'])

for key in dictionary:
    print('the', key, 'is', dictionary[key])
    

print(dictionary.keys())    

print([ x for x in dictionary.keys()])   

print([ x for x in dictionary.values()])  

#update dict

dict1={}

dict1['entry1'] = 'value1'
dict1['entry2'] = 'value2' 
print(dict1)


dict2 = {'key1':1, 'key2': 2}
dict3 = {'key2':3, 'key4': 4}

dict3.update(dict2)
print(dict3)
#update the original value when there is contradiction

dict4 = {'key5':5, 'key6': 6}

dict5={}

for i in [dict2, dict3, dict4]:
    dict5.update(i)

print(dict5)    #look out the order of updaing the same key values


dictionary = {'color':'yellow', 'num_core': 8, 'ram':32}

print(dictionary.get('color', 'no match'))

print(dictionary.get('weight', 'no match'))

word = 'success'

dict7 = {}

for i in word:
    if i not in dict7.keys():
       dict7[i] = 1
    else:
        dict7[i]+=1

print(dict7)        
        

word = 'success'        
charlist = list(word) 

print(charlist)       
        
charset = set(charlist) 

dict8={}

for i in charset:
    dict8[i] = charlist.count(i)
       
print(dict8)        
        

######################################################3


dict9={}
for i in range(1,11):
    dict9[i]=i**2 

print(dict9)       
        
dict10 = {'data1':100, 'data2':-42, 'data3':123}
result = 1
for i in dict10.values():
    result*=i #result = result*i
    
print(result)    


################################List of tuple

x = [(1,2),(3,4),(5,6)]       
print(dict(x)) 
        
        
keys=['width','length','depth'] 
values = [30,40,50]   

for i in zip(keys, values):
    print(i)
        
#print(dict(zip(keys,values)))   


dict11 = {'data1':100, 'data2':-42, 'data3':123}

if 'data1' in dict11.keys():
    del dict11['data1']
        
print(dict11)        
        

dictionary1 = {'color':'yellow', 'num_core': 8, 'ram':32}
                
print(sorted(dictionary1))        


####################################Remove duplicates
dictionary1 = {'color':'yellow', 'num_core': 8, 'ram':32, 'interior':'yellow'}
unique = {}
for i in dictionary1.items():
    key, value = i
    if value not in unique.values():
        unique[key]=value
       
print(unique)        


######################################tuples

tuple1 = 1,2,3,4,5

print(tuple1) 

       
tuple2 = (1,2,3,4,5)

print(tuple2)    


word='success'
print(tuple(word))


print(tuple1[1:3])
print(tuple1[-1])
print(tuple1[2:])


t1 =('1', 'apple')
t2 = ('1','application')

print(t2>t1)





dict20={}
for i in range(1,15):
    dict20[i]=i**2 

print(dict20)


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
{'a': 400, 'b': 400, 'c': 300, 'd': 400}

d4 = {}



print(d1)

tuple3 = 3,4,5
x,y,z=tuple3
print(x)
print(y)
print(z)

x,y,z=z,y,x

##############################set

x = {1,2,3,3}

print(x)

x.add(4)

y = {5,6}

x.update(y)    
        
print(x)        
        
x.remove(1)        
        
print(x)        
        
i=set(['green', 'blue'])   
j=set(['blue','yellow'])

print(i | j)

#print(i&j)


k=set(['green', 'blue'])   
l=set(['blue','yellow'])

kl = k-l
lk = l-k

print(kl)
print(lk)


##############################3functions
def f_to_c(f):
    c=(f-32)*5/9
    return c

print(f_to_c(100))

def function(x):
    for i in range(10):
        if i>x:
            return i
    return x    


print(function(6))

def funct_list(lst, value):
    result = [x for x in lst if x % value == 0]
    return result

print(funct_list([20,30,40,50,60], 3))

#reverse a string

def reverse_str(str):
    result = ''
    for i in x:
        result = i + result
    return result


print(reverse_str('apple'))    

def palindrome(x):
    left=0
    right=len(x)-1
    while right>left and x[left]!=x[right]:
        left+1
        right-=1
        return "no"
    return 'yes'

print(palindrome('yelley'))
        
########use the above reverse function too

###############

import statistics
def avgsales(*sales):
    return statistics.mean(sales)

print(avgsales(1,2,3,4,5,6))



































     