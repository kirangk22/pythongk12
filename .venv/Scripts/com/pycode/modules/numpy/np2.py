

# without numpy
a=[1,2,3,4]
sqrt=[n**2 for n in a]
print(sqrt)

# using numpy
import numpy as np

na=np.array(a)
print(na**2)