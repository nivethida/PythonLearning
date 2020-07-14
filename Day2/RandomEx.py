# -*- coding: utf-8 -*-

import random as r
import numpy as np
"uniformly distributed random num from 0 to 1"

print(r.random())
print(r.random()*4+2)


"random normally distributed number"
print(r.normalvariate(2,4))

"an array of random num (uniform)"

print(np.random.random(5))
print(sum(np.random.random(100)))

print(np.random.rand(3,5))

print(np.random.randn(2,4))# standard normal distribution

x = [1,2,3,4]
y = r.choice(x)
print(y)

x = [1,2,3,4]
y = r.choices(x, k=4)
print(y)

h = r.choices(['rainy','cloudy','sunny'], [0.7,0.2,0.1], k=10)
print(h)

g = r.choices([1,2,3,4,5,6], k= 10).count(6)
print(g)

i = [1,2,3,4]
j = r.sample(i,2)
print(y)

l = [1,2,3,4,6,7]

r.shuffle(l)

print(l)