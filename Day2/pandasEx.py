# -*- coding: utf-8 -*-
import pandas as pd
lst1 = [1,2,3,4,5]

df = pd.DataFrame(lst1)
print(df)  

lst2 = [[1,2,3,4],
       [3,4,5,6]]

df2 = pd.DataFrame(lst2)

print(df2)

df2.columns = ['first','second','third','fourth']

print(df2)

#Dictionary
data = {'studentId': [1,2,3,4,5],
        'dept': ['mgmt', 'finance', 'marketing', 'operations', 'bsna'],
        'age': ['32','29', '34', '23','34']}

print(data)

#converting dict to dataframe
df3 = pd.DataFrame(data)

print(df3)

df4 = df3[['studentId', 'age']]

print(df4)

df5 = df4['studentId']# not data frame but data series

print(df5, type(df5))

print(df4, type(df4))

print(df4.loc[4])
print(df5[1]) #data series access method differs

"No two diemtional series to extract multiple columns use another data frame"


"*****************************************************************************************"


"importing data from another source"

import pandas as pd
import os
#os.chdir('') id the file is in another directory

df6 = pd.read_csv('nba.csv', index_col='Name')
#print(df6)

data3 = {'studentId': [1,2,3,4,5],
        'dept': ['mgmt', 'finance', 'marketing', 'operations', 'bsna'],
        'age': ['32','29', '34', '23','34']}

df7 = pd.DataFrame(data3)
#print(df7)
print(df7.loc[1], '\n')
print(df7.iloc[0])

print(df7.iloc[0,2])

#
print(df7.loc[df7['studentId']>=2], ['dept', 'age'])


print(df7.loc[3:,['studentId','age']])

"*****************************************************************************************"

"Joining two data frames"
import pandas as pd
df8 = pd.DataFrame({'studentId': [1,2,3,4,5],
        'dept': ['finance', 'finance', 'marketing', 'operations', 'bsna']})
df9 = pd.DataFrame({'studentId': [1,2,3,6,7],
                    'gender': ['F', 'F', 'M', 'M', 'F']})

print(df8)
print(df9)

df10 = pd.merge(df8, df9, on='studentId', how = 'inner')

print(df10)

df11 = pd.merge(df8, df9, on='studentId', how = 'outer')

print(df11)

df12 = pd.merge(df8, df9, on='studentId', how = 'right')

print(df12)

df13 = pd.concat(df8, df9, sort=False)

print(df13)