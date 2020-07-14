import os
path = '/Users/nivethida/PythonWorkouts/Day5'
os.chdir(path)

with open('test.txt','r') as f:
    contents = f.read()
    print(contents)
   
    
with open('test.txt','r') as f:
    chunk_size = 5
    chunk = f.read(chunk_size)
    while len(chunk)>0:
        print(chunk)
        chunk=f.read(chunk_size)
        
with open('test.txt','r') as f:
    c=f.read(5)
    while len(c)>0:
        print(c)
        c=f.read(5)
         
        
with open('test.txt','r') as f:
    f_contents=f.readlines()
    print(f_contents)
    
 
with open('test.txt','r') as f:	
    print(f.closed)
print(f.closed)    
    
with open('test.txt','r') as f:
    f_content=f.read()
    print(f_content)
    

with open('test.txt','r') as f:
    f_content=f.readline(10)
    print(f_content)
    f_content=f.readline()
    print(f_content.strip('\n'))    
        
with open('test.txt','r') as f:
    f_contents=f.readlines(10)
    print(f_contents)
    
with open('test2.txt','w') as f:
    f.write('Test contents new ones')


with open('test2.txt','a') as f:
    f.write('\n Test contents new ones line 2')    
    
    

with open('test2.txt','r') as f:
     print(f.tell())
     contents = f.readline(5)
     print(contents)
     f.seek(10)
     print(f.tell())
     #print(f.read(5))
     f.write('python')
     

with open('test.txt','r') as rf:
     with open('test3.txt','w') as wf:
         for line in rf:
             wf.write(line)




import os
path = '/Users/nivethida/PythonWorkouts/Day5'
os.chdir(path)
retval = os.getcwd()
print( "Directory changed successfully %s" % retval)

for i in os.listdir() :
    if i.endswith('.0'):
        print(i)
        newname=i[:-1]+'txt'
        os.rename(i,newname)
        

path = '/Users/nivethida/PythonWorkouts/Day5/test'
os.chdir(path)        
        
outputfile = open('output.txt', 'w')
headers = 'thread_id'+ '\t' + 'creator'+'\t'+'num_views'+'\t'+'num_messages'+'\n'
outputfile.write(headers)

     
for i in os.listdir():
    if i.endswith('.txt') and not i.startswith('output'):
        with open(i, 'r') as f:
            contents = f.readlines()
            threadid = i[:-4]
            creator=contents[4].strip('\n')
            num_view=contents[2].strip('\n')
            num_messages=len(contents)-9
        value_to_insert = str(threadid)+'\t'+str(creator)+'\t'+str(num_view)+'\t'+str(num_messages)+'\n'
        outputfile.write(value_to_insert)
outputfile.close()

       

with open('test2.txt','w') as f:
    f.write('Text')
    f.seek(1)#set the position to the second one
    f.write('Text')
    


print('%s->%d;' % ('cat', 3))
print('%s->%d;' % ('cat', 2) )#missing argument error
print('%d' % 3)    

print('%d' % 4.5)#remember %d is an integer number
print('%f' % 1.234) # floating number, but with 6 digits by default
print('%.2f' % 1.234) # check out the outputs
print('%.3f' % 1.234) # check out the outputs
print('%.4f' % 1.234) #





class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()


































