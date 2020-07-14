# -*- coding: utf-8 -*-
with open('/Users/nivethida/PythonWorkouts/Day5/Lab5.txt', 'r') as f:
    contents = [i.rstrip() for i in f] # rstrip removes the chracters 
    print(contents)




import os.path
os.chdir('/Users/nivethida/PythonWorkouts/Day5')

os.mkdir("F1")

list1 = ["line 1", "line 2", "line 3"]

with open('F1/Insidefile.txt','w') as f:
    for line in list1:
        f.write(line)
        f.write("\n")
f.close()


duplicateStr = "apple"
uniqueStr =  "".join(dict.fromkeys(duplicateStr))
print(uniqueStr)


string_1 = "what"
string_2="where" 


common = set(string_1) & set(string_2)


str1 = ''.join([i for i in string_1 if i not in common])

str2 = ''.join([i for i in string_2 if i not in common])

print(str1+str2)