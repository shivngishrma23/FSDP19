# -*- coding: utf-8 -*-
import numpy as np
import random 
from collections import Counter
l1= np.random.randint(5,15,40)
print(l1)

frequency = Counter(l1)
print (frequency)
maximum = Counter.most_common(frequency)
print(maximum)

maximum= maximum[0][0]
print (maximum)