# -*- coding: utf-8 -*-

class Boss:
    
    salary = 10000
    
    def __init__(self,name,attitude,face):
        self.name = name
        self.attitude=attitude
        self.face=face
        
    def get_name(self):
        print(self.name)
        
    def get_attitude(self):
        print(self.attitude) 
        
    def get_face(self):
        print(self.face)  
        
        
class SmallBoss(Boss):
    
    def __init__(self, name, attitude, face, dept):
        super().__init__(name,attitude,face)
        self.dept=dept
        

class BigBoss(Boss):
    
     def __init__(self, name, attitude, face, manage=None):
        super().__init__(name,attitude,face)
        if manage is None:
            self.manage = []
            
        else:
            self.manage = manage
            
     def add_smallboss(self, smallboss):
         if smallboss not in self.manage:
             self.manage.append(smallboss)
            
     def delete_smallboss(self,smallboss):
         if smallboss in self.manage:
             self.manage.remove(smallboss)    
            
     def show_team(self):
         for i in self.manage:
             i.get_name()
            

smallboss1 = SmallBoss('x', 'positive', 'happy', 'mgmt')           
smallboss2 = SmallBoss('y', 'negative', 'hated', 'fin')  
bigboss1 = BigBoss('z', 'neutral', 'unhappy', [smallboss1])

bigboss1.show_team()            
        
bigboss1.add_smallboss(smallboss2)

bigboss1.show_team()       
        
bigboss1.delete_smallboss(bigboss1,smallboss1)  

bigboss.show_team()      
        


class First(object):
    def __init__(self):
        print("first")

class Second(object):
    def __init__(self):
        print("second")

class Third(First, Second):
    thirdName = "jelly"   
    def __init__(self):
        super().__init__()
        print("that's it")

    
c = Third()
print(c.thirdName)
print(Third.thirdName) 
c.thirdName = "chocolate"
print(c.thirdName) 
print(Third.thirdName)
Third.thirdName = "icecream" 
print(Third.thirdName)        
print(c.thirdName)       
  
b = Third()  
print(b.thirdName)     
        


import pandas as pd
import numpy as np
import math
dictionary = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
df=pd.DataFrame(dictionary)
print(df)
df2=df.loc[df['First Score']>=0,['Second Score', 'Third Score']]
print(df2)


class First(object):
    def __init__(self):
         print("first1")
         super().__init__()
         print("first2")
         

class Second(object):
    def __init__(self):
         print("second1")
         super().__init__()
         print("second2")

class Third(Second, First):
    def __init__(self):
         print("third1")
         super().__init__()
         print("third2")
     
        
c = Third()     

x=[1,2,3]
y=[4,5,6]
z=[(x,y) for x,y in zip(x,y)]
print(z)       
        

word='success' 
dictionary={} # define an empty dictionary, get ready for entries.
for c in word:
     if c not in dictionary: # if the dictionary has not pick up the key
          dictionary[c]=1 # create the key and set the value to 1 because this is the first occurrence
     else: # if the dictionary has already picked up the key
          dictionary[c]=dictionary[c]+ 1 # add 1 to the current value due to another occurrence.
print(dictionary)
        
        
        
        
        
        
        
        
        
        
                