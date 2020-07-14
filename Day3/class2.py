# -*- coding: utf-8 -*-

import random
import numpy as np
result = 0
for i in range(0, 10000):
    x=random.choices(['hit', 'miss'], [1,9], k= 50)
    if x.count('hit') >= 10:
        result += 1
print(result/10000)

x=[56,32,21,8,56,21,35]
for index,value in enumerate(x):
    if value in x[:index]:
        print(index)