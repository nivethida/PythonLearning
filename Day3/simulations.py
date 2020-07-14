# -*- coding: utf-8 -*-

# draw 20 cards from a deck

# how many ten cards are you expecting in 20 draws

import random
import statistics
import matplotlib.pyplot as plt
counter = []
averagecounter = []
for i in range(0, 10000):
    output = random.choices(['ten_cards', 'others_cards'], [16, 36], k = 20)
    counter.append(output.count('ten_cards'))
    averagecounter.append(statistics.mean(counter))
plt.plot(range(0, 1000), averagecounter)
plt.show()
print(statistics.mean(counter))




drug = [54, 73, 53, 70, 73, 68, 52, 65, 65]
placebo = [54, 51, 58, 44, 55, 52, 42, 47, 58, 46]

real_diff = statistics.mean(drug)-statistics.mean(placebo)
fullsample = drug+placebo

print(fullsample) 

for i in range(0, 10000):
    random.shuffle(fullsample)
    sample_drug = statistics.mean(permutation[:len(drug)]) 
    sample_placebo = statictics.mean(permutation[len(drug):])
    sample_diff = sample_drug - sample_placebo
    if sample_diff<real_diff:
        result.append(1)
    else:
        result.append(0)
print(sum(result)/10000)        
        



             
    