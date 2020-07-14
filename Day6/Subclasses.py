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
        

#class GoodBoss(Boss):
#    salary = 20000
#    pass

class GoodBoss(Boss):

    def __init__(self,name,attitude,face,fans):
        super().__init__(name,attitude,face)
        self.fans = fans
    
class BadBoss(Boss):
    def __init__(self,name,attitude,face,howbad = None):
        super().__init__(name,attitude,face)
        self.howbad = howbad
    
    def describe(self):
        if self.howbad is None:
            return "n/a"
        else:
            return self.howbad
        

#boss1 = Boss("x","positive","happy")
#
#print(boss1.face)
#
#boss1.get_attitude()        
#
#
##boss2 = GoodBoss("y","negative","angry")
#
##print(boss2.name)
#
##boss2.get_face
#
#print(boss1.salary)
#
#boss3 = goodBoss("g","positive","happy","a lot")
#print(boss3.fans)
            

boss1 = BadBoss("g","negative","angry","to the bone") 

boss1.get_face()  

print(boss1.describe())     

