class Dog:
   
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def description(self):
        print("the dog named{} is {} years old".format(self.name, self.age))
    
    def bark(self,sound):
        print("{} saids {}, {}".format(self.name, sound, sound))
    
    

jake = dog("jake", 2)
jake.description
jake.bark("gruff")

jake.age = 3
jake.description()
    